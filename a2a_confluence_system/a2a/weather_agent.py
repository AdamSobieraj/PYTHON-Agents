# weather_agent.py
from a2a import Agent, Card

agent = Agent(
    card=Card(
        id="weather-agent",
        name="Weather Agent",
        description="Dostarcza prognozę pogody",
        tools=["get_weather"]  # deklaruje korzystanie z narzędzia MCP
    ),
    mcp_host="http://localhost:5001"
)

@agent.on_message
async def handle(msg):
    city = msg["city"]
    result = await agent.call_tool("get_weather", {"city": city})
    return {"weather": result}

agent.run()
