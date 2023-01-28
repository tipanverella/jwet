CC=poetry
PYTHONFILES=jwet
TESTFILES=tests
GIT=git


install:
	$(CC) install

black: $(PYTHONFILES)
	export PYTHONDONTWRITEBYTECODE=1
	$(CC) run black .

lint: $(PYTHONFILES)
	export PYTHONDONTWRITEBYTECODE=1
	$(CC) run pylint $(PYTHONFILES)

test: 
	export PYTHONDONTWRITEBYTECODE=1
	$(CC) run pytest -vv

blt: black lint test

build: $(PYTHONFILES) mypy coverage
	export PYTHONDONTWRITEBYTECODE=1
	$(CC) version patch
	$(CC) update
	$(CC) build

mypy:
	export PYTHONDONTWRITEBYTECODE=1
	$(CC) run mypy $(PYTHONFILES)

coverage:
	export PYTHONDONTWRITEBYTECODE=1
	$(CC) run pytest -vv --cov=$(PYTHONFILES) --cov-report=term --cov-report=html

push: lint build
	$(GIT) add -A
	$(GIT) commit -m "$(CM)"
	$(GIT) push origin


.PHONY: black lint test 
