from fastmcp import FastMCP
import requests
from dotenv import load_dotenv
import os
from typing import Dict, Optional

load_dotenv()
VAULT_URL = os.getenv("VAULT_URL")
API_TOKEN = os.getenv("API_TOKEN")
VERIFY_SSL = os.getenv("VERIFY_SSL", "true").lower() == "true"

DEFAULT_HEADERS = {
    "Authorization": f"Bearer {API_TOKEN}",
    "Accept": "text/markdown"
}

mcp = FastMCP("Obsidian server")

def vault_request(method: str, file_path: str, content: Optional[str] = None) -> Dict:
    url = f"{VAULT_URL}/{file_path}"
    headers = DEFAULT_HEADERS.copy()
    if content is not None:
        headers["Content-Type"] = "text/markdown"
    try:
        response = requests.request(
            method.upper(),
            url,
            headers=headers,
            data=content,
            verify=VERIFY_SSL
        )
        return {
            "status": response.status_code,
            "headers": dict(response.headers),
            "body": response.text
        }
    except Exception as e:
        return {"error": str(e), "method": method, "url": url}

@mcp.tool()
def read_file(file_path: str) -> Dict:
    return vault_request("GET", file_path)

@mcp.tool()
def add_file(file_path: str, content: str) -> Dict:
    return vault_request("POST", file_path, content)

@mcp.tool()
def write_file(file_path: str, content: str) -> Dict:
    return vault_request("PUT", file_path, content)

@mcp.tool()
def delete_file(file_path: str) -> Dict:
    return vault_request("DELETE", file_path)

@mcp.tool()
def http_request(method: str, url: str, headers: Optional[Dict] = None, data: Optional[Dict] = None) -> Dict:
    try:
        response = requests.request(
            method.upper(),
            url,
            headers=headers,
            json=data,
            verify=VERIFY_SSL
        )
        return {
            "status": response.status_code,
            "headers": dict(response.headers),
            "body": response.text
        }
    except Exception as e:
        return {"error": str(e), "method": method, "url": url}

if __name__ == "__main__":
    mcp.run()
