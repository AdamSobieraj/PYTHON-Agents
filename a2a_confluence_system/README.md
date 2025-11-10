# 🤖 A2A Confluence + OpenAI System

System z dwoma agentami zgodnymi z protokołem **A2A**:

1. **Confluence Fetcher Agent** – pobiera dane z Confluence (lub z mockowych danych).  
2. **Analyzer Agent** – analizuje treści stron Confluence za pomocą **OpenAI GPT** i zwraca streszczenie.  

Całość działa lokalnie w **Docker Compose**.

---

## 📁 Struktura projektu

a2a_confluence_system/
│
├── agent_confluence/
│ ├── config.py
│ ├── confluence_integration.py
│ ├── main.py
│ ├── mock_data/pages.json
│ └── generate_mock_data.py
│
├── agent_analyzer/
│ ├── config.py
│ └── main.py
│
├── requirements.txt
├── Dockerfile.confluence
├── Dockerfile.analyzer
├── docker-compose.yml
└── README.md


---

## ⚙️ Wymagania

- Python 3.11+
- Docker i Docker Compose
- Klucz **OpenAI API** (`OPENAI_API_KEY`)
- (Opcjonalnie) konto Atlassian z dostępem do Confluence

---

## 🐳 Uruchamianie lokalne z mockami

1. Wygeneruj przykładowe strony Confluence:
```bash
python agent_confluence/generate_mock_data.py
```
Uruchom system w Docker Compose:

docker-compose up --build

Confluence Fetcher Agent: http://localhost:8000

Analyzer Agent: http://localhost:8001

Upewnij się, że w docker-compose.yml jest ustawione:

environment:
  - MOCK_MODE=true


Dzięki temu agent Confluence będzie korzystał z mockowych danych zamiast prawdziwego API.