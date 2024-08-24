import requests
import pandas as pd
from io import StringIO
from .exceptions import PIPAPIError
from .server import current_server


def get_aux(
    table=None,
    version=None,
    ppp_version=None,
    release_version=None,
    format="json",
    assign_tb=False,
):
    """
    Retrieve auxiliary data from the World Bank's PIP API.

    Args:
        table (str, optional): Name of the auxiliary table to retrieve.
        version (str, optional): Version of the data to retrieve.
        ppp_version (str, optional): Version of PPP to use.
        release_version (str, optional): Release version of the data.
        format (str): Format of the returned data. Defaults to 'json'.
        assign_tb (bool): Whether to assign the data to a global variable. Defaults to False.

    Returns:
        pandas.DataFrame: A DataFrame containing the requested auxiliary data.

    Raises:
        PIPAPIError: If the API request fails or returns unexpected data.
    """
    if table is None:
        response = requests.get(f"{current_server}/aux")
        return response.json()

    params = {
        k: v
        for k, v in locals().items()
        if v is not None and k not in ["assign_tb"]
    }

    try:
        response = requests.get(f"{current_server}/aux", params=params)
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


def get_countries(**kwargs):
    """
    Retrieve a list of countries from the World Bank's PIP API.

    Args:
        **kwargs: Additional keyword arguments to pass to get_aux().

    Returns:
        pandas.DataFrame: A DataFrame containing the list of countries.

    Raises:
        PIPAPIError: If the API request fails or returns unexpected data.
    """
    return get_aux("countries", **kwargs)


def get_regions(**kwargs):
    """
    Retrieve a list of regions from the World Bank's PIP API.

    Args:
        **kwargs: Additional keyword arguments to pass to get_aux().

    Returns:
        pandas.DataFrame: A DataFrame containing the list of regions.

    Raises:
        PIPAPIError: If the API request fails or returns unexpected data.
    """
    return get_aux("regions", **kwargs)


def get_cpi(**kwargs):
    """
    Retrieve Consumer Price Index (CPI) data from the World Bank's PIP API.

    Args:
        **kwargs: Additional keyword arguments to pass to get_aux().

    Returns:
        pandas.DataFrame: A DataFrame containing the CPI data.

    Raises:
        PIPAPIError: If the API request fails or returns unexpected data.
    """
    return get_aux("cpi", **kwargs)


def get_dictionary(**kwargs):
    """
    Retrieve the data dictionary from the World Bank's PIP API.

    Args:
        **kwargs: Additional keyword arguments to pass to get_aux().

    Returns:
        pandas.DataFrame: A DataFrame containing the data dictionary.

    Raises:
        PIPAPIError: If the API request fails or returns unexpected data.
    """
    return get_aux("dictionary", **kwargs)


def get_gdp(**kwargs):
    """
    Retrieve Gross Domestic Product (GDP) data from the World Bank's PIP API.

    Args:
        **kwargs: Additional keyword arguments to pass to get_aux().

    Returns:
        pandas.DataFrame: A DataFrame containing the GDP data.

    Raises:
        PIPAPIError: If the API request fails or returns unexpected data.
    """
    return get_aux("gdp", **kwargs)
