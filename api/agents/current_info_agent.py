"""
Current Information agent for handling news and current event queries.
"""

from typing import Literal
from langgraph.types import Command
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage
from api.graph.state import State
from api.tools.external_tools import initialize_external_tools
from api.config.prompts import CURRENT_INFO_PROMPT


def create_current_info_agent(llm_model):
    """
    Create the current information agent and node.
    
    Args:
        llm_model: The LLM model to use for the agent
        
    Returns:
        tuple: (agent, node_function)
    """
    # Initialize external tools
    external_tools = initialize_external_tools()
    
    # Create the agent
    agent = create_react_agent(
        llm_model, 
        [external_tools["tavily_search"]],
        prompt=CURRENT_INFO_PROMPT
    )
    
    # Define the node function
    def current_info_node(state: State) -> Command[Literal["supervisor"]]:
        """
        Process queries related to current news and events.
        
        Args:
            state (State): The current state
            
        Returns:
            Command: Command with the agent's response
        """
        result = agent.invoke(state)
        return Command(
            update={
                "messages": [
                    HumanMessage(content=result["messages"][-1].content, name="current_info_agent")
                ]
            },
            goto="supervisor",
        )
    
    return agent, current_info_node