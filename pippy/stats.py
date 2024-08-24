import requests
import pandas as pd
import json
from io import StringIO
from .constants import BASE_URL
from .exceptions import PIPAPIError


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
):
    """
    Get poverty and inequality statistics.

    :param country: A string or list of country ISO 3 codes, or 'all'
    :param year: An integer, list of years, or 'all'
    :param povline: Poverty line (default is 2.15)
    :param popshare: Proportion of the population living below the poverty line
    :param fill_gaps: If True, will interpolate / extrapolate values for missing years
    :param subgroup: If used, result will be aggregated for predefined sub-groups
    :param welfare_type: Welfare type, one of 'all', 'income', or 'consumption'
    :param reporting_level: Geographical reporting level, one of 'all', 'national', 'urban', or 'rural'
    :param version: Data version
    :param ppp_version: PPP year to be used
    :param release_version: Date when the data was published in YYYYMMDD format
    :param format: Response format, one of 'json', 'csv', or 'rds'
    :param debug: If True, prints debug information
    :return: Pandas DataFrame
    """
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
        response = requests.get(url, params=params)
        if debug:
            print(f"Response status code: {response.status_code}")
            print(f"Response headers: {response.headers}")
            print(
                f"Raw response content: {response.text[:1000]}..."
            )  # Print first 1000 characters of raw content
        response.raise_for_status()
    except requests.RequestException as e:
        if debug:
            print(f"Request exception: {str(e)}")
            print(f"Response content: {response.text[:1000]}...")
        raise PIPAPIError(
            f"API request failed: {str(e)}\nResponse content: {response.text[:1000]}..."
        )

    content_type = response.headers.get("Content-Type", "")
    if debug:
        print(f"Content-Type: {content_type}")

    if "text/html" in content_type:
        error_msg = f"API returned an HTML error page. Status code: {response.status_code}\n"
        error_msg += f"Response content: {response.text[:1000]}..."
        if debug:
            print(error_msg)
        raise PIPAPIError(error_msg)

    if format == "json":
        try:
            data = response.json()
            if debug:
                print(f"JSON data: {json.dumps(data, indent=2)[:500]}...")
            return (
                pd.DataFrame(data)
                if isinstance(data, list)
                else pd.DataFrame([data])
            )
        except json.JSONDecodeError:
            if debug:
                print("Failed to parse JSON")
            raise PIPAPIError(
                f"API returned invalid JSON. Raw content: {response.text[:1000]}..."
            )
    elif format == "csv":
        try:
            df = pd.read_csv(StringIO(response.text))
            if debug:
                print(f"DataFrame shape: {df.shape}")
                print(f"DataFrame columns: {df.columns}")
            return df
        except pd.errors.EmptyDataError:
            if debug:
                print("Empty DataFrame")
            raise PIPAPIError("API returned an empty CSV")
    else:
        return response.content  # For RDS format


def get_wb(
    year="all",
    povline=2.15,
    version=None,
    ppp_version=None,
    release_version=None,
    format="json",
):
    """
    Get World Bank global and regional aggregates.

    :param year: An integer, list of years, or 'all'
    :param povline: Poverty line (default is 2.15)
    :param version: Data version
    :param ppp_version: PPP year to be used
    :param release_version: Date when the data was published in YYYYMMDD format
    :param format: Response format, one of 'json', 'csv', or 'rds'
    :return: Pandas DataFrame
    """
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
