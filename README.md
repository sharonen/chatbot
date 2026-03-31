# Chatbot

An AI-powered research chatbot built with Claude that searches and retrieves academic papers from arXiv. Includes an MCP (Model Context Protocol) server for tool-based paper research.

## Project Structure

```
chatbot/
├── requirements.txt          # Python dependencies
├── mcp_project/
│   ├── research_server.py    # MCP server exposing arXiv search tools
│   ├── mcp_chatbot.py        # MCP-enabled chatbot client
│   └── pyproject.toml
```

## Features

- Search arXiv for academic papers by topic
- Retrieve stored paper metadata by paper ID
- Interactive chat loop powered by Claude (`claude-sonnet-4-6`)
- MCP server/client architecture for tool use

## Requirements

- Python >= 3.10
- An Anthropic API key

## Setup

1. Clone the repo and install dependencies:

```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the project root:

```
ANTHROPIC_API_KEY=sk-ant-...
```

## MCP Project

The `mcp_project` folder contains an MCP server and chatbot client.

### Setup

```bash
cd mcp_project
uv venv --python 3.14
source .venv/bin/activate
uv add mcp arxiv anthropic python-dotenv
```

### Run the chatbot

```bash
uv run mcp_chatbot.py
```

### Run with MCP Inspector

```bash
npx @modelcontextprotocol/inspector uv run research_server.py
```

## Available Tools

| Tool | Description |
|------|-------------|
| `search_papers(topic, max_results)` | Search arXiv for papers on a topic, saves results locally |
| `extract_info(paper_id)` | Retrieve stored metadata for a paper by its ID |
