"""
Search tools for the agents to use.
"""

from langchain_core.tools import tool
from api.services.vector_store import initialize_vector_store


# Initialize the vector store
vector_store = initialize_vector_store()


@tool
def search_resmi_gazete(query: str) -> str:
    """
    Resmi Gazete vektör veritabanında arama yapar.

    Args:
        query (str): Aranacak metin

    Returns:
        str: Arama sonuçları (içerik + metadata)
    """
    results = vector_store.similarity_search(query, k=1)

    if not results:
        return "Resmi Gazete veritabanında ilgili bir bilgi bulunamadı."

    formatted_results = []
    for doc in results:
        tarih = doc.metadata.get("tarih", "tarih bilinmiyor")
        sayi = doc.metadata.get("sayi", "sayı bilinmiyor")
        formatted_results.append(
            f"Tarih: {tarih} | Sayı: {sayi}\n{doc.page_content}"
        )

    return "\n\n---\n\n".join(formatted_results)
