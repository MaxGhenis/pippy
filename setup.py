from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pippy",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python package for accessing World Bank's Poverty and Inequality Platform (PIP) API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pippy",
    packages=find_packages(exclude=["tests", "docs"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.10",
    install_requires=[
        "requests>=2.26.0",
        "pandas>=1.3.3",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=22.0",
            "build>=0.7",
        ],
        "docs": [
            "mkdocs>=1.3",
            "mkdocs-material>=8.0",
            "mkdocstrings[python]>=0.19",
        ],
    },
    entry_points={
        "console_scripts": [
            "pippy=pippy.cli:main",
        ],
    },
)
