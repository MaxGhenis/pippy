# Getting Started with pippy

## Installation

You can install pippy using pip:

```bash
pip install pippy
```

## Basic Usage

Here's a quick example of how to use pippy:

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

For more detailed examples, check out the [Examples](examples/basic-usage.md) section.
