.PHONY: install install-dev install-docs test build docs lint format all

install:
	pip install -e .

install-dev:
	pip install -e ".[dev]"

install-docs:
	pip install -e ".[docs]"

test:
	python -m pytest tests/ --cov=pippy --cov-report=xml

build:
	python -m build

docs:
	mkdocs build

lint:
	black . -l 79 --check

format:
	black . -l 79

all: install-dev test build docs