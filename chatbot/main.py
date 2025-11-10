from fastapi import FastAPI, Request
import requests
from .jira_integration import get_recent_jira_issues
from .openai_agent import analyze_tickets

app = FastAPI(title="OpenAI A2A Jira Agent")

@app.get("/")
def root():
    return {"status": "running", "agent": "jira+openai"}

@app.post("/process")
async def process(request: Request):
    data = await request.json()
    task = data.get("task", "").lower()

    # Pobranie danych z Jira
    if "jira" in task or "ticket" in task:
        issues = get_recent_jira_issues()
        ai_summary = analyze_tickets(issues)
        return {"status": "ok", "data": issues, "ai_summary": ai_summary}

    # Komunikacja A2A z innym agentem
    if "query" in data:
        target = data["query"].get("target")
        query_task = data["query"].get("task")
        response = requests.post(f"http://{target}/process", json={"task": query_task})
        return {"status": "ok", "response": response.json()}

    return {"status": "ok", "result": f"Nieznane polecenie: {task}"}
