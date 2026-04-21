import requests

API = "http://127.0.0.1:8000"


def fetch_targets(timeout=1.0):
    try:
        resp = requests.get(f"{API}/targets", timeout=timeout)
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return []