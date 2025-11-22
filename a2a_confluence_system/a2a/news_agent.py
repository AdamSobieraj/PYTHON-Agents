# news_agent.py
from a2a import Agent, Card

agent = Agent(
    card=Card(
        id="news-agent",
        name="News Agent",
        description="Udostępnia najnowsze wiadomości",
        tools=["get_news"]
    ),
    mcp_host="http://localhost:5001"
)

@agent.on_message
async def handle(msg):
    result = await agent.call_tool("get_news", {})
    return {"news": result}

agent.run()
