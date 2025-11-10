from openai import OpenAI
from .config import OPENAI_API_KEY, A2A_AGENT_NAME, A2A_SERVER_PORT
from .a2a import Server, Message

client = OpenAI(api_key=OPENAI_API_KEY)
server = Server(name=A2A_AGENT_NAME, port=A2A_SERVER_PORT)

@server.handle("task.analyze.docs")
async def handle_analysis(message: Message):
    pages = message.payload.get("pages", [])
    content = "\n\n".join([f"{p['title']}:\n{p['content']}" for p in pages])

    prompt = f"""
Oto strony dokumentacji Confluence:
{content}

Przygotuj syntetyczne streszczenie:
- główne tematy,
- powtarzające się zagadnienia,
- potencjalne luki / ryzyka w dokumentacji.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Jesteś asystentem ds. analizy dokumentacji technicznej."},
            {"role": "user", "content": prompt},
        ],
    )

    summary = response.choices[0].message.content.strip()
    await message.reply({"summary": summary})

if __name__ == "__main__":
    server.run()
