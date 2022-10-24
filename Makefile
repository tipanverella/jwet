CC=poetry
PYTHONFILES=jwet
TESTFILES=tests
GIT=git


install:
	$(CC) install

black: $(PYTHONFILES)
	$(CC) run black .

lint: $(PYTHONFILES)
	$(CC) run pylint $(PYTHONFILES)

test: 
	$(CC) run pytest -vv

blt: black lint test

build: $(PYTHONFILES) mypy coverage
	$(CC) version patch
	$(CC) update
	$(CC) build

mypy:
	$(CC) run mypy $(PYTHONFILES)

coverage:
	$(CC) run pytest -vv --cov=$(PYTHONFILES) --cov-report=term --cov-report=html

push: lint build
	$(GIT) add -A
	$(GIT) commit -m "$(CM)"
	$(GIT) push origin


.PHONY: black lint test 