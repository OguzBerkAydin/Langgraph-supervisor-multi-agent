"""
Graph builder for creating the LangGraph application flow.
"""

from langgraph.graph import StateGraph, START, END
from api.graph.state import State


def build_graph(supervisor_node, agent_nodes):
    """
    Build the LangGraph graph with nodes and edges.
    
    Args:
        supervisor_node: The supervisor node function
        agent_nodes (dict): Dictionary of agent node functions
        
    Returns:
        StateGraph: The compiled graph
    """

    builder = StateGraph(State)
    

    builder.add_node("supervisor", supervisor_node)
    builder.add_node("official_newspaper_agent", agent_nodes["official_newspaper_agent"])
    builder.add_node("fallback_agent", agent_nodes["fallback_agent"])
    builder.add_node("current_info_agent", agent_nodes["current_info_agent"])
    

    builder.add_edge(START, "supervisor")

    return builder.compile()