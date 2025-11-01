import requests


def post_to_external_api(url: str, payload: dict) -> dict:
    response = requests.post(url, json=payload, timeout=10)
    print(f"POST {url} status {response.status_code}")
    response.raise_for_status()
    return response.json()


def get_from_external_api(url: str) -> dict:
    response = requests.get(url, timeout=10)
    print(f"GET {url} status {response.status_code}")
    response.raise_for_status()
    return response.json()
