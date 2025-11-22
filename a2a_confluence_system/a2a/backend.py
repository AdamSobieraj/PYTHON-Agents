from python_a2a import A2AClient
from fastapi import FastAPI

app = FastAPI()
client = A2AClient("http://localhost:agent-port/a2a")

@app.get("/weather")
async def weather(city: str, ip: str):
    response = client.send_message({
        "content": {"text": f"Pytanie o pogodę w {city} i IP {ip}"}
    })
    return {"result": response}
