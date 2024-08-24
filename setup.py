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
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.10",
    install_requires=[
        "requests",
        "pandas",
    ],
)
