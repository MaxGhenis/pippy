import requests
from .constants import BASE_URL
from .exceptions import PIPAPIError


def check_api_status():
    endpoints = {
        "pip": f"{BASE_URL}/pip",
        "pip-info": f"{BASE_URL}/pip-info",
        "health-check": f"{BASE_URL}/health-check",
    }

    status = {}
    for name, url in endpoints.items():
        try:
            response = requests.get(url)
            if (
                response.status_code == 200
                and not response.text.strip().startswith("<html>")
            ):
                status[name] = "OK"
            else:
                status[name] = f"Error (Status: {response.status_code})"
        except requests.RequestException:
            status[name] = "Connection Error"

    return status


def check_api(api_version="v1"):
    try:
        response = requests.get(f"{BASE_URL}/health-check")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise PIPAPIError(f"API health check failed: {str(e)}")


def get_versions(api_version="v1"):
    try:
        response = requests.get(f"{BASE_URL}/versions")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise PIPAPIError(f"Failed to retrieve versions: {str(e)}")


def get_pip_info(api_version="v1"):
    try:
        response = requests.get(f"{BASE_URL}/pip-info")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise PIPAPIError(f"Failed to retrieve PIP info: {str(e)}")
