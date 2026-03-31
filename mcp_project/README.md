# MCP Research Server

An MCP (Model Context Protocol) server that lets AI assistants search and retrieve academic papers from arXiv.

## Tools

- **`search_papers(topic, max_results)`** — Search arXiv for papers on a given topic. Saves results locally as JSON. Returns a list of paper IDs.
- **`extract_info(paper_id)`** — Retrieve stored metadata for a paper by its ID (e.g. `1312.3300v1`).

## Requirements

- Python >= 3.10
- [uv](https://docs.astral.sh/uv/)

## Setup

```bash
cd mcp_project

# Create and activate virtual environment
uv venv
source .venv/bin/activate

# Install dependencies
uv add mcp arxiv anthropic python-dotenv nest_asyncio
```

## Run the MCP server

### With MCP Inspector

```bash
npx @modelcontextprotocol/inspector uv run research_server.py
```

### Directly 

```bash
uv run research_server.py
```

## Run the MCP Chatbot
```bash
uv run mcp_chatbot.py
```