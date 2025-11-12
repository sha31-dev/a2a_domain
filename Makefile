.PHONY: all black build clean coverage install mypy package pylint test

all: black pylint mypy clean 
package: build install

black:
	@echo "Running black..."
	black --config=pyproject.toml .

build:
	@echo "Bundling package..."
	rm -rf dist/ && poetry build

clean:
	@echo "Cleaning up..."
	find . -name "__pycache__" -type d -exec rm -rf {} +
	find . -name ".pytest_cache" -type d -exec rm -rf {} +

coverage:
	@echo "Running coverage..."
	coverage run -m --source=a2a_domain/ pytest tests/ -v && coverage report -m

install:
	@echo "Bundling package..."
	pip install dist/a2a_domain-*.tar.gz

mypy:
	@echo "Running mypy..."
	mypy --config=pyproject.toml a2a_domain/ tests/

pylint:
	@echo "Running pylint..."
	pylint --rcfile=./pyproject.toml a2a_domain/ tests/

test:
	@echo "Running unit tests..."
	pytest tests/ -s -v