"""
Main entry point for the LangGraph application.
This file initializes all components and runs the application.
"""

from api.models.llm_models import initialize_llm_models
from api.agents.supervisor import create_supervisor_node
from api.agents.official_gazette_agent import create_official_gazette_agent
from api.agents.fallback_agent import create_fallback_agent
from api.agents.current_info_agent import create_current_info_agent
from api.graph.graph_builder import build_graph


def main():
    """
    Initialize and run the LangGraph application.
    """
    print("Initializing models...")
    llm_qwen, llm_llama, llm_openai = initialize_llm_models()
    
    print("Creating agents...")
    # Create supervisor node using OpenAI model for routing
    supervisor_node = create_supervisor_node(llm_openai)
    
    # Create agent nodes using Qwen model for responses
    _, official_gazette_node = create_official_gazette_agent(llm_qwen)
    _, fallback_node = create_fallback_agent(llm_qwen)
    _, current_info_node = create_current_info_agent(llm_qwen)
    
    # Organize agent nodes
    agent_nodes = {
        "official_newspaper_agent": official_gazette_node,
        "fallback_agent": fallback_node,
        "current_info_agent": current_info_node
    }
    
    print("Building graph...")
    graph = build_graph(supervisor_node, agent_nodes)
    
    print("System ready. Enter your question (or 'exit' to quit):")
    
    while True:
        # Get user input
        user_input = input("> ")
        
        if user_input.lower() == "exit":
            break
        
        print("Processing query...")
        # Run the graph with the user input
        for s in graph.stream(
            {"messages": [("user", user_input)]}, subgraphs=True
        ):
            # Use this for debugging if needed
            print(s)
            print("----")
            pass
        
        print("---")


if __name__ == "__main__":
    main()