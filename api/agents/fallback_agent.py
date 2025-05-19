"""
Fallback agent for handling out-of-scope queries.
"""

from typing import Literal
from langgraph.types import Command
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import HumanMessage
from api.graph.state import State
from api.config.prompts import FALLBACK_PROMPT


def create_fallback_agent(llm_model):
    """
    Create the fallback agent and node.
    
    Args:
        llm_model: The LLM model to use for the agent
        
    Returns:
        tuple: (agent, node_function)
    """
    # Create the agent
    agent = create_react_agent(
        llm_model, 
        [],  # No tools needed for fallback
        prompt=FALLBACK_PROMPT
    )
    
    # Define the node function
    def fallback_node(state: State) -> Command[Literal["supervisor"]]:
        """
        Handle out-of-scope queries with explanations about system limitations.
        
        Args:
            state (State): The current state
            
        Returns:
            Command: Command with the agent's response
        """
        result = agent.invoke(state)
        return Command(
            update={
                "messages": [
                    HumanMessage(content=result["messages"][-1].content, name="fallback_agent")
                ]
            },
            goto="supervisor",
        )
    
    return agent, fallback_node