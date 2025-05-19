"""
External API tools for the agents to use.
"""

from langchain_community.tools.tavily_search import TavilySearchResults


def initialize_external_tools():
    """
    Initialize and return external tools.
    
    Returns:
        dict: Dictionary of external tools
    """
    
    tavily_tool = TavilySearchResults(max_results=2)
    
    return {
        "tavily_search": tavily_tool
    }