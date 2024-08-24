import requests
import pandas as pd
import logging
from .exceptions import PIPAPIError
from .cache import cache_response, get_cached_response
from .server import current_server, set_server
from .logger import pippy_logger


def get_stats(
    country="all",
    year="all",
    povline=None,
    popshare=None,
    fill_gaps=False,
    region=None,
    welfare_type="all",
    reporting_level="all",
    ppp_version=None,
    release_version=None,
    format="json",
    group_by=None,
    debug=False,
    use_cache=True,
):
    if debug:
        pippy_logger.setLevel(logging.DEBUG)
    else:
        pippy_logger.setLevel(logging.INFO)

    pippy_logger.debug("Debug mode enabled")

    cache_key = f"stats_{country}_{year}_{povline}_{popshare}_{welfare_type}_{reporting_level}_{ppp_version}_{release_version}"

    if use_cache:
        cached_data = get_cached_response(cache_key)
        if cached_data:
            pippy_logger.debug("Using cached data")
            return pd.DataFrame(cached_data)

    endpoint = "pip-grp" if group_by else "pip"
    url = f"{current_server}/{endpoint}"

    params = {
        "country": country if country != "all" else "ALL",
        "year": year if year != "all" else "ALL",
        "povline": povline,
        "popshare": popshare,
        "fill_gaps": "true" if fill_gaps else None,
        "welfare_type": welfare_type,
        "reporting_level": reporting_level,
        "ppp_version": ppp_version,
        "release_version": release_version,
        "format": format,
    }

    if region:
        params["country"] = region

    if group_by:
        params["group_by"] = "wb" if group_by == "wb" else "none"

    # Remove None values
    params = {k: v for k, v in params.items() if v is not None}

    pippy_logger.debug(f"Request URL: {url}")
    pippy_logger.debug(f"Request params: {params}")

    try:
        response = requests.get(url, params=params, timeout=10)
        pippy_logger.debug(f"Response status code: {response.status_code}")
        pippy_logger.debug(f"Response headers: {response.headers}")
        pippy_logger.debug(f"Raw response content: {response.text[:1000]}...")
        response.raise_for_status()

        content_type = response.headers.get("Content-Type", "")
        if "application/json" not in content_type:
            if "<html>" in response.text[:100]:
                raise PIPAPIError(
                    "API returned an HTML error page. The service may be experiencing issues."
                )
            else:
                raise PIPAPIError(
                    f"Unexpected content type: {content_type}. Full response: {response.text[:1000]}..."
                )

        data = response.json()
        df = (
            pd.DataFrame(data)
            if isinstance(data, list)
            else pd.DataFrame([data])
        )

        if use_cache:
            cache_response(cache_key, data)

        return df
    except requests.RequestException as e:
        pippy_logger.error(f"API request failed: {str(e)}")
        if isinstance(e, requests.HTTPError) and e.response.status_code == 500:
            raise PIPAPIError(
                "The API server encountered an internal error. Please try again later or contact the API maintainers."
            )
        raise PIPAPIError(
            f"API request failed: {str(e)}\nResponse content: {getattr(e.response, 'text', '')[:1000]}..."
        )
    except ValueError as e:
        pippy_logger.error(f"Failed to parse API response: {str(e)}")
        raise PIPAPIError(f"Failed to parse API response: {str(e)}")


def get_wb(
    year="all",
    povline=None,
    ppp_version=None,
    release_version=None,
    format="json",
):
    return get_stats(
        country="all",
        year=year,
        povline=povline,
        group_by="wb",
        ppp_version=ppp_version,
        release_version=release_version,
        format=format,
    )


# Ensure the server is set correctly
set_server()
