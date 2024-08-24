from .stats import get_stats, get_wb
from .aux import (
    get_aux,
    get_countries,
    get_regions,
    get_cpi,
    get_dictionary,
    get_gdp,
)
from .utils import check_api, get_versions, get_pip_info
from .exceptions import PIPAPIError

__version__ = "0.1.0"
