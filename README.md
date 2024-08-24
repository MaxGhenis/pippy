# pippy

pippy is a Python package for accessing the World Bank's Poverty and Inequality Platform (PIP) API. It provides an easy-to-use interface for retrieving poverty and inequality statistics, as well as auxiliary data.

## Installation

You can install pippy using pip:

```
pip install pippy
```

## Example

This is a basic example that shows how to retrieve some key poverty and inequality statistics.

### Retrieve statistics

```python
import pippy

# Get poverty statistics for Albania
df = pippy.get_stats(country="ALB")
print(df.head())

# Get World Bank global/regional stats
wb_stats = pippy.get_wb(year="all")
print(wb_stats.head())
```

### Access data dictionary

```python
dictionary = pippy.get_dictionary()
print(dictionary.head())
```

## Available Functions

- `get_stats()`: Get poverty and inequality statistics
- `get_wb()`: Get World Bank global and regional aggregates
- `get_aux()`: Get auxiliary data
- `get_countries()`: Get country information
- `get_regions()`: Get region information
- `get_cpi()`: Get Consumer Price Index data
- `get_dictionary()`: Get data dictionary
- `get_gdp()`: Get Gross Domestic Product data
- `check_api()`: Check API status
- `get_versions()`: Get available data versions
- `get_pip_info()`: Get information about the API

## Error Handling

The package uses a custom `PIPAPIError` exception to handle API-specific errors. Always wrap your API calls in a try-except block to handle potential errors gracefully.

```python
try:
    stats = pippy.get_stats(country="ALB")
except pippy.api.PIPAPIError as e:
    print(f"An error occurred: {str(e)}")
```

## Citation

To cite package `pippy` in publications, please use:

      [Your Name] (2023). pippy: Python Client for the PIP API. https://github.com/[your_username]/pippy

A BibTeX entry for LaTeX users is:

      @Manual{,
        title = {pippy: Python Client for the PIP API},
        author = {[Your Name]},
        year = {2023},
        note = {https://github.com/[your_username]/pippy},
      }

## License

This project is licensed under the MIT License - see the LICENSE file for details.
