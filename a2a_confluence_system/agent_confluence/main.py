from .a2a import Server, Client, Message
from .config import A2A_SERVER_PORT, A2A_AGENT_NAME, ANALYZER_URL
from .confluence_integration import fetch_recent_pages

server = Server(name=A2A_AGENT_NAME, port=A2A_SERVER_PORT)
client = Client(ANALYZER_URL)

@server.handle("task.confluence.fetch")
async def handle_confluence_task(message: Message):
    pages = fetch_recent_pages(limit=5)
    print(f"Pobrano {len(pages)} stron z Confluence")

    analysis = await client.send("task.analyze.docs", payload={"pages": pages})

    await message.reply({
        "fetched_pages": len(pages),
        "analysis": analysis,
    })
    print("Wynik wysłany użytkownikowi")

if __name__ == "__main__":
    server.run()
