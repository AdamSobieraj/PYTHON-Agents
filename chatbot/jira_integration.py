import requests
from requests.auth import HTTPBasicAuth
from .config import ATLASSIAN_URL, JIRA_USER, JIRA_API_TOKEN

def get_recent_jira_issues(jql="project = TEST ORDER BY created DESC", limit=5):
    """Pobiera ostatnie tickety z Jira (MCP Atlassiana)."""
    url = f"{ATLASSIAN_URL}/rest/api/3/search"
    response = requests.get(
        url,
        params={"jql": jql, "maxResults": limit},
        auth=HTTPBasicAuth(JIRA_USER, JIRA_API_TOKEN),
        headers={"Accept": "application/json"},
    )
    if response.status_code != 200:
        return {"error": response.text}
    data = response.json()
    return [
        {
            "key": issue["key"],
            "summary": issue["fields"]["summary"],
            "status": issue["fields"]["status"]["name"],
        }
        for issue in data.get("issues", [])
    ]
