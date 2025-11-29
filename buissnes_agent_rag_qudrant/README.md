# Przykładowy Asystent Sklepu RAG + Qdrant + LangChain + OpenAI

System asystenta sklepu z elektroniką wykorzystujący technikę **RAG (Retrieval-Augmented Generation)**.  
Model odpowiada wyłącznie na podstawie danych zapisanych w bazie wektorowej **Qdrant**, korzystając z pipeline’u **LangChain (LCEL)**.

---

## 🚀 Funkcjonalności

- automatyczne ładowanie wiedzy z pliku tekstowego  
- generowanie embeddingów i zapis w Qdrant  
- wyszukiwanie wektorowe (similarity search)  
- odpowiedzi generowane przez GPT-4o-mini  
- prompting i pipeline z LangChain  
- asystent odpowiada WYŁĄCZNIE na podstawie kontekstu  

---

## 📦 Wymagane biblioteki

```
pip install qdrant-client langchain langchain-openai openai numpy pandas
```
🗄️ Uruchomienie Qdrant (Docker)

```
docker compose up
```

📊 RAG — schemat działania

[1] Użytkownik → pytanie \
[2] Embedding pytania \
[3] Wyszukiwanie wektorowe w Qdrant \
[4] LangChain: prompt + kontekst \
[5] GPT generuje odpowiedź \
[6] Finalna odpowiedź dla użytkownika 


