# time_agent.py
from a2a import Agent, Card

agent = Agent(
    card=Card(
        id="time-agent",
        name="Time Agent",
        description="Zwraca aktualny czas",
        tools=["get_time"]
    ),
    mcp_host="http://localhost:5001"
)

@agent.on_message
async def handle(msg):
    result = await agent.call_tool("get_time", {})
    return {"time": result}

agent.run()
