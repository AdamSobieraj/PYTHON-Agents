# orchestrator_agent.py
from a2a import Agent

agent = Agent(
    card={
        "id": "main-orchestrator",
        "name": "Orchestrator",
        "description": "Koordynuje wszystkie agentowe zapytania"
    }
)

@agent.on_message
async def handle(msg):
    city = msg["city"]
    ip = msg["ip"]

    weather = await agent.send("weather-agent", {"city": city})
    location = await agent.send("location-agent", {"ip": ip})
    time = await agent.send("time-agent", {})
    news = await agent.send("news-agent", {})

    return {
        "city": city,
        "weather": weather,
        "location": location,
        "time": time,
        "news": news
    }

agent.run()
