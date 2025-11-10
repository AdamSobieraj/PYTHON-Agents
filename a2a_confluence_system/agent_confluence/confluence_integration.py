import json
import os
import requests
from requests.auth import HTTPBasicAuth
from .config import ATLASSIAN_URL, ATLASSIAN_USER, ATLASSIAN_API_TOKEN, MOCK_MODE, MOCK_PATH

def fetch_recent_pages(limit=3):
    """Pobiera strony z Confluence lub z mocka jeśli MOCK_MODE=True"""
    if MOCK_MODE and os.path.exists(MOCK_PATH):
        with open(MOCK_PATH, encoding="utf-8") as f:
            pages = json.load(f)
        print(f"🧪 Tryb MOCK: załadowano {len(pages)} stron z pliku.")
        return pages[:limit]

    # tryb produkcyjny
    url = f"{ATLASSIAN_URL}/rest/api/content"
    response = requests.get(
        url,
        params={"limit": limit, "expand": "body.storage"},
        auth=HTTPBasicAuth(ATLASSIAN_USER, ATLASSIAN_API_TOKEN),
        headers={"Accept": "application/json"},
    )

    if response.status_code != 200:
        return {"error": response.text}

    data = response.json()
    return [
        {"id": p["id"], "title": p["title"], "content": p["body"]["storage"]["value"]}
        for p in data.get("results", [])
    ]
