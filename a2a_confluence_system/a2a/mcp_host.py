from mcp.server.fastmcp import FastMCP
import httpx
import datetime

mcp = FastMCP("example-mcp-host")

@mcp.tool()
def get_weather(city: str) -> str:
    resp = httpx.get(f"https://wttr.in/{city}?format=j1")
    return resp.text

@mcp.tool()
def lookup_ip(ip: str) -> str:
    # Jeśli nie używasz geoip, możesz zwrócić cokolwiek
    return f"Lokalizacja dla IP {ip} (dummy)"

@mcp.tool()
def get_time() -> str:
    return str(datetime.datetime.now())

@mcp.tool()
def get_news() -> str:
    resp = httpx.get("https://newsapi.org/api/top-headlines?country=us&apiKey=XYZ")
    return resp.text

if __name__ == "__main__":
    mcp.run()
