# location_agent.py
from a2a import Agent, Card

agent = Agent(
    card=Card(
        id="location-agent",
        name="Location Agent",
        description="Dostarcza geolokalizację",
        tools=["lookup_ip"]
    ),
    mcp_host="http://localhost:5001"
)

@agent.on_message
async def handle(msg):
    ip = msg["ip"]
    result = await agent.call_tool("lookup_ip", {"ip": ip})
    return {"location": result}

agent.run()
