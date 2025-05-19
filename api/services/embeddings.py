"""
Embedding model service for text embeddings.
"""

#from langchain_huggingface import HuggingFaceEmbeddings
from api.config.settings import EMBEDDINGS_MODEL
from langchain_openai import OpenAIEmbeddings


# def get_embedding_model():
#     """
#     Initialize and return the embedding model.
    
#     Returns:
#         HuggingFaceEmbeddings: Initialized embedding model
#     """
#     return HuggingFaceEmbeddings(model_name=EMBEDDINGS_MODEL)

def get_openai_embedding_model():
    """
    Initialize and return the OpenAI embedding model.
    
    Returns:
        OpenAIEmbeddings: Initialized OpenAI embedding model
    """
    return OpenAIEmbeddings(model=EMBEDDINGS_MODEL)