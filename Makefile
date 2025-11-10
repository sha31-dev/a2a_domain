.PHONY: all black clean install mypy pylint

all: black pylint mypy clean

black:
	@echo "Running black..."
	black --config=pyproject.toml .

clean:
	@echo "Cleaning up..."
	find . -name "__pycache__" -type d -exec rm -rf {} +
	find . -name ".pytest_cache" -type d -exec rm -rf {} +

mypy:
	@echo "Running mypy..."
	mypy --config=pyproject.toml .

pylint:
	@echo "Running pylint..."
	pylint --rcfile=./pyproject.toml .
