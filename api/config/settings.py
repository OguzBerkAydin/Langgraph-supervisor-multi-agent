"""
Configuration settings for the application.
Handles environment variables and API keys.
"""
import os
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# API Keys
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
TAVILY_API_KEY = os.environ.get("TAVILY_API_KEY")

# Set environment variables for libraries that need them
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["TAVILY_API_KEY"] = TAVILY_API_KEY
os.environ["GROQ_API_KEY"] = GROQ_API_KEY

# Model Names
QWEN_MODEL = "llama3-70b-8192"
LLAMA_MODEL = "llama-3.3-70b-versatile"
GPT_MODEL = "gpt-4o-mini"

# Vector Database Settings
EMBEDDINGS_MODEL = "text-embedding-ada-002"
VECTOR_DB_COLLECTION = "resmi_gazete_embeddings_4092"
VECTOR_DB_PERSIST_DIR = "api/resmi_gazete_chroma_4092"

# Agent Names
OFFICIAL_GAZETTE_AGENT = "official_newspaper_agent"
FALLBACK_AGENT = "fallback_agent"
CURRENT_INFO_AGENT = "current_info_agent"

# Available agents for router
AGENT_MEMBERS = [OFFICIAL_GAZETTE_AGENT, FALLBACK_AGENT, CURRENT_INFO_AGENT]
ROUTER_OPTIONS = AGENT_MEMBERS + ["FINISH"]