# Basic Usage of pippy

This guide demonstrates the basic usage of the pippy package for accessing the World Bank's Poverty and Inequality Platform (PIP) API.

## Installation

First, install pippy using pip:

```bash
pip install pippy
```

## Importing pippy

Start by importing the pippy package:

```python
import pippy
```

## Retrieving Poverty Statistics

### Get statistics for a specific country

To get poverty statistics for a specific country, use the `get_stats()` function:

```python
# Get poverty statistics for Albania
albania_stats = pippy.get_stats(country="ALB")
print(albania_stats.head())
```

This will return a DataFrame with poverty statistics for Albania.

### Get World Bank global/regional statistics

To retrieve World Bank global or regional statistics, use the `get_wb()` function:

```python
# Get World Bank global/regional stats for all years
wb_stats = pippy.get_wb(year="all")
print(wb_stats.head())
```

## Accessing Auxiliary Data

pippy also provides functions to access various auxiliary data:

### Get list of countries

```python
countries = pippy.get_countries()
print(countries.head())
```

### Get list of regions

```python
regions = pippy.get_regions()
print(regions.head())
```

### Get CPI data

```python
cpi_data = pippy.get_cpi()
print(cpi_data.head())
```

## Working with Different Data Versions

You can retrieve information about available data versions:

```python
versions = pippy.get_versions()
print(versions)
```

To use a specific data version, pass it to the `version` parameter:

```python
# Select the first available version
selected_version = versions[0]['version']

# Get statistics for Angola using the selected version
angola_stats = pippy.get_stats(country="AGO", release_version=selected_version)
print(angola_stats.head())
```

## Error Handling

pippy uses custom exceptions to handle errors. Always wrap your API calls in try-except blocks:

```python
from pippy import PIPAPIError

try:
    invalid_country_stats = pippy.get_stats(country="INVALID")
except PIPAPIError as e:
    print(f"An error occurred: {str(e)}")
```

This basic usage guide covers the main functionalities of pippy. For more detailed information about each function and its parameters, please refer to the API Reference section.
