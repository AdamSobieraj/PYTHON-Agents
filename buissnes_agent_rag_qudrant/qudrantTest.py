from qdrant_client import QdrantClient
from dotenv import load_dotenv
import os

# Wczytanie zmiennych środowiskowych
load_dotenv()

# Parametry
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

# Połączenie z Qdrant
qdrant = QdrantClient(host="localhost", port=6333)

def list_collection_contents(collection_name):
    # scroll zwraca krotkę (points, next_page)
    points, _ = qdrant.scroll(
        collection_name=collection_name,
        limit=1000
    )

    for point in points:
        text = point.payload.get("text", "")  # payload to dict
        print(f"ID: {point.id}, Text: {text}")

if __name__ == "__main__":
    list_collection_contents(COLLECTION_NAME)
