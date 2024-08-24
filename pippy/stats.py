import requests
import pandas as pd
import json
from io import StringIO
from .constants import BASE_URL
from .exceptions import PIPAPIError
from .cache import cache_response, get_cached_response


def get_stats(
    country="all",
    year="all",
    povline=2.15,
    popshare=None,
    fill_gaps=False,
    subgroup=None,
    welfare_type="all",
    reporting_level="all",
    version=None,
    ppp_version=None,
    release_version=None,
    format="json",
    debug=False,
    use_cache=True,
):
    cache_key = f"stats_{country}_{year}_{povline}_{welfare_type}_{reporting_level}_{version}_{ppp_version}_{release_version}"

    if use_cache:
        cached_data = get_cached_response(cache_key)
        if cached_data:
            return pd.DataFrame(cached_data)

    endpoint = "pip" if subgroup is None else "pip-grp"
    params = {
        k: v
        for k, v in locals().items()
        if v is not None and k not in ["subgroup", "debug"]
    }

    if subgroup:
        params["group_by"] = "wb" if subgroup == "wb_regions" else subgroup

    url = f"{BASE_URL}/{endpoint}"

    if debug:
        print(f"Request URL: {url}")
        print(f"Request params: {params}")

    try:
        response = requests.get(url, params=params, timeout=10)
        if debug:
            print(f"Response status code: {response.status_code}")
            print(f"Response headers: {response.headers}")
            print(f"Raw response content: {response.text[:1000]}...")
        response.raise_for_status()

        if (
            "text/html" in response.headers.get("Content-Type", "")
            or "<html>" in response.text[:100]
        ):
            raise PIPAPIError(
                "API returned HTML instead of expected JSON. The service may be experiencing issues."
            )

        data = response.json()
        df = (
            pd.DataFrame(data)
            if isinstance(data, list)
            else pd.DataFrame([data])
        )
        cache_response(cache_key, data)
        return df
    except requests.RequestException as e:
        if debug:
            print(f"Request exception: {str(e)}")
            print(f"Response content: {response.text[:1000]}...")
        raise PIPAPIError(f"API request failed: {str(e)}")
    except ValueError as e:
        if debug:
            print(f"Failed to parse response: {str(e)}")
        raise PIPAPIError(f"Failed to parse API response: {str(e)}")


def get_wb(
    year="all",
    povline=2.15,
    version=None,
    ppp_version=None,
    release_version=None,
    format="json",
):
    return get_stats(
        country="all",
        year=year,
        povline=povline,
        subgroup="wb_regions",
        version=version,
        ppp_version=ppp_version,
        release_version=release_version,
        format=format,
    )
