import requests
from .exceptions import PIPAPIError
from .server import current_server


def check_api_status():
    """
    Check the status of different API endpoints.

    Returns:
        dict: A dictionary with the status of each endpoint.
    """
    endpoints = {
        "pip": f"{current_server}/pip",
        "pip-info": f"{current_server}/pip-info",
        "health-check": f"{current_server}/health-check",
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

    Args:
        api_version (str): API version. Defaults to "v1".

    Returns:
        dict: API status information.

    Raises:
        PIPAPIError: If the API health check fails.
    """
    try:
        response = requests.get(f"{current_server}/health-check")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise PIPAPIError(f"API health check failed: {str(e)}")


def get_versions(api_version="v1"):
    """
    Get available data versions.

    Args:
        api_version (str): API version. Defaults to "v1".

    Returns:
        dict: Available data versions.

    Raises:
        PIPAPIError: If the request to retrieve versions fails.
    """
    try:
        response = requests.get(f"{current_server}/versions")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise PIPAPIError(f"Failed to retrieve versions: {str(e)}")


def get_pip_info(api_version="v1"):
    """
    Get information about the API.

    Args:
        api_version (str): API version. Defaults to "v1".

    Returns:
        dict: API information.

    Raises:
        PIPAPIError: If the request to retrieve PIP info fails.
    """
    try:
        response = requests.get(f"{current_server}/pip-info")
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise PIPAPIError(f"Failed to retrieve PIP info: {str(e)}")
