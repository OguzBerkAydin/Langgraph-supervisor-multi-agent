from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse

from api.models.llm_models import initialize_llm_models
from api.agents.supervisor import create_supervisor_node
from api.agents.official_gazette_agent import create_official_gazette_agent
from api.agents.fallback_agent import create_fallback_agent
from api.agents.current_info_agent import create_current_info_agent
from api.graph.graph_builder import build_graph

# FastAPI uygulamasını oluştur
app = FastAPI()

# İstek modeli
class ChatRequest(BaseModel):
    message: str
    debug: bool = False

# Başlatma işlemleri (sadece bir kez yapılır)
print("Initializing models...")
llm_qwen, llm_llama, llm_openai = initialize_llm_models()

print("Creating agents...")
supervisor_node = create_supervisor_node(llm_openai)
_, official_gazette_node = create_official_gazette_agent(llm_openai)
_, fallback_node = create_fallback_agent(llm_qwen)
_, current_info_node = create_current_info_agent(llm_qwen)

agent_nodes = {
    "official_newspaper_agent": official_gazette_node,
    "fallback_agent": fallback_node,
    "current_info_agent": current_info_node
}

print("Building graph...")
graph = build_graph(supervisor_node, agent_nodes)

@app.post("/analyze_chat")
async def analyze_chat(request: ChatRequest):
    """
    Kullanıcıdan gelen mesajı işleyip anlamlı bir yanıt döndürür.
    """
    user_input = request.message
    try:
        # Tüm adımları topla
        steps = []
        final_response = None
        
        for step in graph.stream({"messages": [("user", user_input)]}, subgraphs=True):
            steps.append(step)
            
            # Bir agent'ın son mesajını kontrol et
            if isinstance(step, tuple) and len(step) == 2 and isinstance(step[1], dict):
                for agent_key in ['official_newspaper_agent', 'current_info_agent', 'fallback_agent']:
                    if agent_key in step[1] and 'messages' in step[1][agent_key]:
                        messages = step[1][agent_key]['messages']
                        if messages and isinstance(messages[0].content, str):
                            final_response = messages[0].content
        
        # Eğer debug=True ise tüm adımları da döndür
        debug = request.debug if hasattr(request, "debug") else False
        
        if debug:
            return JSONResponse(content={
                "response": final_response,
                "steps": [str(step) for step in steps]
            })
        else:
            return JSONResponse(content={"response": final_response})
            
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
