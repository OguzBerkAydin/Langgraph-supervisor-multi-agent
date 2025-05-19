"""
Vector store service for document retrieval.
"""

from langchain_chroma import Chroma
#from api.services.embeddings import get_embedding_model
from api.services.embeddings import get_openai_embedding_model
from api.config.settings import VECTOR_DB_COLLECTION, VECTOR_DB_PERSIST_DIR


def initialize_vector_store():
    """
    Initialize and return the vector store for document retrieval.
    
    Returns:
        Chroma: Initialized vector store
    """
    #embeddings = get_embedding_model()
    
    embeddings = get_openai_embedding_model()

    # Load the vector database
    vector_store = Chroma(
        collection_name=VECTOR_DB_COLLECTION,
        embedding_function=embeddings,
        persist_directory=VECTOR_DB_PERSIST_DIR
    )
    
    return vector_store