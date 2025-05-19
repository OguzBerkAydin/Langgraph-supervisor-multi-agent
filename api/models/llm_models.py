"""
LLM model configurations for the application.
"""

from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI
from api.config.settings import (
    GROQ_API_KEY,
    OPENAI_API_KEY,
    QWEN_MODEL,
    LLAMA_MODEL,
    GPT_MODEL,
)


def initialize_llm_models():
    """
    Initialize and return LLM models used by the application.
    
    Returns:
        tuple: Three LLM models - qwen, llama, and openai
    """
    # Initialize Qwen model via Groq
    llm_qwen = ChatGroq(
        temperature=0,
        model_name=QWEN_MODEL,
        api_key=GROQ_API_KEY
    )
    
    # Initialize Llama model via Groq
    llm_llama = ChatGroq(
        temperature=0,
        model_name=LLAMA_MODEL,
        api_key=GROQ_API_KEY
    )
    
    # Initialize OpenAI model
    llm_openai = ChatOpenAI(
        model=GPT_MODEL, 
        temperature=0
    )
    
    return llm_qwen, llm_llama, llm_openai