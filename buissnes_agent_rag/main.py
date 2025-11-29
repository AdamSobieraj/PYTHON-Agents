from openai import OpenAI
from SearchKnowledgebase import SearchKnowledgebase
from ShopAssistant import ShopAssistant
from dotenv import load_dotenv
import os

load_dotenv()

def init_openai(api_key: str):
    return OpenAI(api_key=api_key)

if __name__ == "__main__":
    API_KEY = os.getenv("OPENAI_API_KEY")
    KNOWLEDGE_FILE = os.getenv("KNOWLEDGE_FILE")
    client = init_openai(API_KEY)

    if not all([API_KEY, KNOWLEDGE_FILE]):
        raise ValueError("Nie wczytano poprawnie zmiennych z .env")

    # Tworzymy serwis RAG
    search_service = SearchKnowledgebase(client, knowledge_path=KNOWLEDGE_FILE)

    assistant = ShopAssistant(client, search_service)

    print("Asystent sklepu – wpisz 'exit' aby zakończyć.\n")
    while True:
        q = input("Zadaj pytanie: ")
        if q.lower() in ["exit", "quit", "wyjdz", "koniec"]:
            break
        assistant.handle_query(q)
