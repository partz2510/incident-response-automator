import os, requests

def vt_hash_lookup(file_hash):
    key = os.getenv("VT_API_KEY")
    if not key:
        return {"error": "API key not set"}
    url = f"https://www.virustotal.com/api/v3/files/{file_hash}"
    headers = {"x-apikey": key}
    resp = requests.get(url, headers=headers)
    return resp.json() if resp.status_code == 200 else {"error": f"HTTP {resp.status_code}"}
