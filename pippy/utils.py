import requests
from .constants import BASE_URL
from .exceptions import PIPAPIError


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
