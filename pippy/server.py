import requests
from .constants import SERVERS, DEFAULT_SERVER
from .exceptions import PIPAPIError


def set_server(server=DEFAULT_SERVER):
    if server not in SERVERS:
        raise ValueError(
            f"Invalid server: {server}. Choose from {', '.join(SERVERS.keys())}"
        )

    base_url = SERVERS[server]

    # Health check
    try:
        response = requests.get(f"{base_url}/health-check")
        response.raise_for_status()
        if "API is running" not in response.text:
            raise PIPAPIError("API health check failed")
    except requests.RequestException as e:
        raise PIPAPIError(f"Failed to connect to the API: {str(e)}")

    return base_url


current_server = set_server()


def get_base_url():
    return current_server


def get_pip_url():
    return f"{current_server}/pip"


def get_pip_grp_url():
    return f"{current_server}/pip-grp"
