

# Obsidian MCP Server

This project provides an **MCP server** that connects Claude (or any MCP client) to your Obsidian vault through the **Obsidian Local REST API**. It allows you to work with Obsidian directly to edit files and can even write notes in your vault.

---

## Prerequisites

- Python **3.9+**  
- `pip`  
- Obsidian with the **REST API plugin** enabled  
- Claude Desktop (or any other MCP client)  

---

## Setup

Clone or copy this project and ensure the following files are present:

- `obsidian.py` — the MCP server  
- `.env` — configuration values (not checked into git)  
- `requirements.txt`  

---

## Requirements

Create a `requirements.txt` file:


```
fastmcp
requests
python-dotenv
PyPDF2
```

Install dependencies:

```
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```


⸻

## Configuration

Create a .env file in the project root:

```
VAULT_URL=https://127.0.0.1:27124/vault
API_TOKEN=your_api_token_here
```

Update .gitignore to exclude local secrets and environment files:

.env
.venv/


⸻

## Running the Server

### Option 1: Run manually

python -u obsidian.py

### Option 2: Run with inline environment variables

VAULT_URL="https://127.0.0.1:27124/vault" \
API_TOKEN="your_api_token_here" \
python obsidian.py



## Claude Desktop Integration

To connect Claude Desktop, add this server to your MCP config.
Example JSON snippet:
```
{
  "name": "Obsidian MCP Server",
  "command": ["/usr/bin/env", "python3", "-u", "/absolute/path/to/obsidian.py"],
  "cwd": "/absolute/path/to/project",
  "transport": "stdio",
  "env": {
    "VAULT_URL": "https://127.0.0.1:27124/vault",
    "API_TOKEN": "your_api_token_here"
  }
}
```

