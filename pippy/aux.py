import requests
import pandas as pd
from io import StringIO
from .constants import BASE_URL
from .exceptions import PIPAPIError


def get_aux(
    table=None,
    version=None,
    ppp_version=None,
    release_version=None,
    format="json",
    assign_tb=False,
):
    """
    Get auxiliary data.

    :param table: Name of the auxiliary table
    :param version: Data version
    :param ppp_version: PPP year to be used
    :param release_version: Date when the data was published in YYYYMMDD format
    :param format: Response format, one of 'json', 'csv', or 'rds'
    :param assign_tb: If True, assigns the table to a global dictionary
    :return: Pandas DataFrame (for CSV/JSON) or bytes (for RDS)
    """
    if table is None:
        response = requests.get(f"{BASE_URL}/aux")
        return response.json()

    params = {
        k: v
        for k, v in locals().items()
        if v is not None and k not in ["assign_tb"]
    }

    try:
        response = requests.get(f"{BASE_URL}/aux", params=params)
        response.raise_for_status()
    except requests.RequestException as e:
        raise PIPAPIError(f"API request failed: {str(e)}")

    if format == "json":
        data = response.json()
        df = (
            pd.DataFrame(data)
            if isinstance(data, list)
            else pd.DataFrame([data])
        )
    elif format == "csv":
        try:
            df = pd.read_csv(StringIO(response.text))
        except pd.errors.EmptyDataError:
            raise PIPAPIError("API returned an empty CSV")
    else:
        return response.content  # For RDS format

    if assign_tb:
        global aux_data
        if "aux_data" not in globals():
            aux_data = {}
        aux_data[table] = df

    return df


# Shorthand functions for specific auxiliary data
def get_countries(**kwargs):
    return get_aux("countries", **kwargs)


def get_regions(**kwargs):
    return get_aux("regions", **kwargs)


def get_cpi(**kwargs):
    return get_aux("cpi", **kwargs)


def get_dictionary(**kwargs):
    return get_aux("dictionary", **kwargs)


def get_gdp(**kwargs):
    return get_aux("gdp", **kwargs)
