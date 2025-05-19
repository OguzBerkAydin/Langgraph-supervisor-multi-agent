"""
Official Gazette agent for handling queries about official publications.
"""

from typing import Literal
from langgraph.types import Command
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage
from api.graph.state import State
from api.tools.search_tools import search_resmi_gazete
from api.config.prompts import OFFICIAL_GAZETTE_PROMPT


def create_official_gazette_agent(llm_model):
    """
    Create the Official Gazette agent and node.
    
    Args:
        llm_model: The LLM model to use for the agent
        
    Returns:
        tuple: (agent, node_function)
    """
    # Create the agent
    agent = create_react_agent(
        llm_model, 
        [search_resmi_gazete],
        prompt=OFFICIAL_GAZETTE_PROMPT
    )
    
    # Define the node function
    def gazette_node(state: State) -> Command[Literal['supervisor']]:
        """
        Process queries related to the Official Gazette.
        
        Args:
            state (State): The current state
            
        Returns:
            Command: Command with the agent's response
        """
        result = agent.invoke(state)
        return Command(
            update={
                "messages": [
                    HumanMessage(content=result['messages'][-1].content, name="official_newspaper_agent")
                ]
            },
            goto="supervisor",
        )
    
    return agent, gazette_node