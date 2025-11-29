from openai import OpenAI
from SearchKnowledgebase import SearchKnowledgebase
from ShopAssistant import ShopAssistant
from qdrant_client import QdrantClient
from dotenv import load_dotenv
import os

load_dotenv()

def init_openai(api_key: str):
    return OpenAI(api_key=api_key)

def init_qdrant():
    return QdrantClient(url=os.getenv("QDRANT_URL"))

if __name__ == "__main__":

    API_KEY = os.getenv("OPENAI_API_KEY")
    COLLECTION_NAME = os.getenv("COLLECTION_NAME")
    KNOWLEDGE_FILE = os.getenv("KNOWLEDGE_FILE")
    CHAT_MODEL = os.getenv("CHAT_MODEL")
    EMBEDING_MODEL = os.getenv("EMBEDING_MODEL")

    if not all([API_KEY, COLLECTION_NAME, KNOWLEDGE_FILE, CHAT_MODEL, EMBEDING_MODEL]):
        raise ValueError("Nie wczytano poprawnie zmiennych z .env")

    # Inicjalizacja klientów
    client = init_openai(API_KEY)
    qdrant_client = init_qdrant()

    # Tworzymy serwis RAG z Qdrant
    search_service = SearchKnowledgebase(
        client=client,
        knowledge_path=KNOWLEDGE_FILE,
        qdrant_client=qdrant_client,
        collection_name=COLLECTION_NAME,
        embedding_model=EMBEDING_MODEL,
    )

    assistant = ShopAssistant(client, search_service, CHAT_MODEL)

    print("Asystent sklepu – wpisz 'exit' aby zakończyć.\n")
    while True:
        q = input("Zadaj pytanie: ")
        if q.lower() in ["exit", "quit", "wyjdz", "koniec"]:
            break
        assistant.handle_query(q)
