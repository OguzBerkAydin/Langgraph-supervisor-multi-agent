"""
State definitions for the LangGraph.
"""

from typing import Literal
from typing_extensions import TypedDict
from langgraph.graph import MessagesState


class Router(TypedDict):
    """
    Worker to route to next. If no workers needed, route to FINISH.
    """
    next: Literal["official_newspaper_agent", "fallback_agent", "current_info_agent", "FINISH"]


class State(MessagesState):
    """
    State definition for the application.
    """
    next: str
    total_iterations: int