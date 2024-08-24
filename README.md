# pippy

pippy is a Python package for accessing the World Bank's Poverty and Inequality Platform (PIP) API. It provides an easy-to-use interface for retrieving poverty and inequality statistics, as well as auxiliary data.

## Installation

You can install pippy using pip:

```
pip install pippy
```

## Usage

Here's a basic example of how to use pippy:

```python
import pippy

# Get poverty statistics for Albania
df = pippy.get_stats(country="ALB")
print(df.head())

# Get World Bank global/regional stats
wb_stats = pippy.get_wb(year="all")
print(wb_stats.head())

# Get auxiliary data
countries = pippy.get_countries()
print(countries.head())
```

## Running Tests

To run the tests, make sure you have pytest installed and then run:

```
pytest
```

Note that some tests may be skipped if the World Bank API is unavailable.

## Known Limitations

- The package depends on the availability of the World Bank PIP API. If the API is down or experiencing issues, some functions may not work as expected.
- Large data requests may take some time to process.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
