import json
from faker import Faker
import random
import os

fake = Faker("pl_PL")
mock_path = "agent_confluence/mock_data/pages.json"

topics = [
    "Architektura mikroserwisowa",
    "Strategia testowania E2E",
    "CI/CD z GitHub Actions",
    "Bezpieczeństwo API",
    "Optymalizacja zapytań SQL",
]

def generate_fake_page(topic):
    return {
        "id": fake.uuid4(),
        "title": f"Dokumentacja: {topic}",
        "content": f"""
<h1>{topic}</h1>
<p>{fake.paragraph(nb_sentences=3)}</p>
<h2>Opis</h2>
<p>{fake.paragraph(nb_sentences=5)}</p>
<h2>Rekomendacje</h2>
<ul>
<li>{fake.sentence()}</li>
<li>{fake.sentence()}</li>
</ul>
        """,
    }

def generate_pages(n=5):
    return [generate_fake_page(random.choice(topics)) for _ in range(n)]

if __name__ == "__main__":
    os.makedirs(os.path.dirname(mock_path), exist_ok=True)
    pages = generate_pages(5)
    with open(mock_path, "w", encoding="utf-8") as f:
        json.dump(pages, f, ensure_ascii=False, indent=2)
    print(f"Wygenerowano {len(pages)} stron w pliku {mock_path}")
