import requests
from .constants import BASE_URL
from .exceptions import PIPAPIError


def check_api_status():
    """
    Check the status of different API endpoints.

    :return: A dictionary with the status of each endpoint
    """
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
    """
    Check internet connection and API status.

    :param api_version: API version
    :return: API status information
    """
    try:
        response = requests.get(f"{BASE_URL}/health-check")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise PIPAPIError(f"API health check failed: {str(e)}")


def get_versions(api_version="v1"):
    """
    Get available data versions.

    :param api_version: API version
    :return: Available data versions
    """
    try:
        response = requests.get(f"{BASE_URL}/versions")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise PIPAPIError(f"Failed to retrieve versions: {str(e)}")


def get_pip_info(api_version="v1"):
    """
    Get information about the API.

    :param api_version: API version
    :return: API information
    """
    try:
        response = requests.get(f"{BASE_URL}/pip-info")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise PIPAPIError(f"Failed to retrieve PIP info: {str(e)}")
