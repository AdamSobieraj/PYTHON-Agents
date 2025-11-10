from openai import OpenAI
from .config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def analyze_tickets(tickets):
    """
    Analizuje dane z Jira za pomocą OpenAI (GPT-4o).
    """
    if not tickets:
        return {"summary": "Brak danych do analizy."}

    # Format danych do prompta
    issues_text = "\n".join([f"{t['key']}: {t['summary']} (status: {t['status']})" for t in tickets])

    prompt = f"""
    Oto lista zgłoszeń Jira:
    {issues_text}

    Proszę o zwięzłe podsumowanie sytuacji projektowej:
    - Ile zgłoszeń jest otwartych / zamkniętych?
    - Jakie są główne tematy / wzorce w opisach?
    - Jakie potencjalne ryzyka widać?
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Jesteś analitykiem projektów Jira."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.4,
    )

    return {
        "summary": response.choices[0].message.content.strip()
    }
