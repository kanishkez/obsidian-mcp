
Obsidian MCP Server

This project provides an MCP server that connects Claude (or any MCP client) to your Obsidian vault through the Obsidian Local REST API.

⸻

Prerequisites
	•	Python 3.9+
	•	pip
	•	Obsidian with the REST API plugin enabled
	•	Claude Desktop (or other MCP client)

⸻

Setup

Clone or copy this project and ensure the following files are present:
	•	obsidian.py — the MCP server
	•	.env — configuration values (not checked into git)
	•	requirements.txt

⸻

requirements.txt

fastmcp
requests
python-dotenv
PyPDF2

Install dependencies:

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt


⸻

Configuration

Create a .env file in the project root:

VAULT_URL=https://127.0.0.1:27124/vault
API_TOKEN=your_api_token_here

Ignore .env in .gitignore:

.env
.venv/


⸻

Running

Run the server manually:

python -u obsidian.py

Or run with inline environment variables:

VAULT_URL="https://127.0.0.1:27124/vault" API_TOKEN="your_api_token_here" python obsidian.py


⸻

Claude Desktop Integration

Add this server to your Claude MCP config. Example JSON snippet:

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


⸻

Notes
	•	The .env values (VAULT_URL, API_TOKEN) remain valid until you change them in Obsidian.
	•	Claude can now call the exposed tools (read_file, add_file, write_file, delete_file).
