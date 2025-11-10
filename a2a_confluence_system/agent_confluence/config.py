import os

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "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")

ATLASSIAN_URL = os.getenv("ATLASSIAN_URL", "https://twoja-domena.atlassian.net/wiki")
ATLASSIAN_USER = os.getenv("ATLASSIAN_USER", "user@example.com")
ATLASSIAN_API_TOKEN = os.getenv("ATLASSIAN_API_TOKEN", "your_api_token_here")

# A2A
A2A_AGENT_NAME = os.getenv("A2A_AGENT_NAME", "confluence-fetcher")
A2A_SERVER_PORT = int(os.getenv("A2A_SERVER_PORT", 8000))
ANALYZER_URL = os.getenv("ANALYZER_URL", "http://agent-analyzer:8001")

# Mock mode
MOCK_MODE = os.getenv("MOCK_MODE", "true").lower() == "true"
MOCK_PATH = "agent_confluence/mock_data/pages.json"
