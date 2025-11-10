import os

# Konfiguracja Atlassian
ATLASSIAN_URL = os.getenv("ATLASSIAN_URL", "https://<twoja-domena>.atlassian.net")
JIRA_USER = os.getenv("JIRA_USER", "<user@example.com>")
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN", "<token>")

# OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "<openai_api_key>")

# Agent
AGENT_PORT = int(os.getenv("AGENT_PORT", 8000))
AGENT_NAME = os.getenv("AGENT_NAME", "agent-jira")
