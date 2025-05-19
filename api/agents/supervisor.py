"""
Supervisor agent for routing messages to the appropriate agent.
"""

from typing import Literal
from langgraph.types import Command
from api.graph.state import State, Router
from langgraph.graph import StateGraph, MessagesState, START, END
from api.config.prompts import SUPERVISOR_PROMPT


def create_supervisor_node(llm_model):
    """
    Create the supervisor node for routing queries.
    
    Args:
        llm_model: The LLM model to use for the supervisor
        
    Returns:
        function: The supervisor node function
    """
    def supervisor_node(state: State) -> Command[Literal["official_newspaper_agent", "fallback_agent", "current_info_agent", "__end__"]]:
        """
        Process the messages and decide which agent should handle the query.
        
        Args:
            state (State): The current state
            
        Returns:
            Command: Command with the next agent to route to
        """
        if "total_iterations" not in state:
            state["total_iterations"] = 0

        if state["total_iterations"] >= 5:  # 5 maksimum iterasyon sayısı
            print(f"Maksimum iterasyon sayısına ulaşıldı ({state['total_iterations']}). Sonlandırılıyor.")
            return Command(goto=END, update={"next": "FINISH"})

        messages = [
            {"role": "system", "content": SUPERVISOR_PROMPT},
        ] + state["messages"]


        iteration_info = f"\nŞu anki toplam iterasyon sayısı: {state['total_iterations']}. 5 veya daha fazla iterasyon yapıldığında FINISH dönün."
        messages[0]["content"] += iteration_info

        #print("Supervisor input messages:", messages)

        response = llm_model.with_structured_output(Router).invoke(messages)

        #print("Supervisor LLM response:", response)

        if response is None or "next" not in response:
            raise ValueError("LLM response is invalid or missing 'next' key")

        goto = response["next"]
        if goto == "FINISH":
            goto = "__end__"

        state["total_iterations"] = state["total_iterations"] + 1
    
        return Command(goto=goto, update={"next": goto, "total_iterations": state["total_iterations"]})
    
    return supervisor_node