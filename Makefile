# Test and build application

START="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m"
PYTHON_VERSION=3.7.2

OS_TYPE = $(shell uname -s)

ifeq ($(OS_TYPE), Darwin)
	PYTHON_BIN="/usr/local/bin/python3.7"
	PYTHON_VENV="$(shell pwd)/.venv/bin/python"
	POETRY_BIN="${HOME}/.poetry/bin/poetry"
	POETRY_CACHE_DIR=${HOME}/Library/Caches/pypoetry
else
	PYTHON_BIN="${HOME}/.pyenv/versions/$(PYTHON_VERSION)/bin/python"
	PYTHON_VENV="$(shell pwd)/.venv/bin/python"
	POETRY_BIN="${HOME}/.pyenv/versions/$(PYTHON_VERSION)/bin/poetry"
	DISTPATH="$(shell pwd)/dist"
	POETRY_CACHE_DIR=${HOME}/.cache/pypoetry
endif

.PHONY: test-ci

install:
	$(PYTHON_BIN) -m pip install poetry; \
	$(PYTHON_BIN) -m pip install pre-commit; \
	$(POETRY_BIN) config settings.virtualenvs.in-project true || exit 1; \
	$(POETRY_BIN) install || exit 1; \

update:
	$(POETRY_BIN) update || exit 1
	$(POETRY_BIN) export --dev --format requirements.txt || exit 1

generate:
	$(POETRY_BIN) export --dev --format requirements.txt || exit 1

test:
	@echo $(START)'Running tests'$(END)
	$(PYTHON_VENV) -m unittest discover --verbose -s ./tests -t ./tests

test-ci:
	@echo $(START)'Running tests on CI'$(END)
	python -m unittest discover --verbose -s ./tests -t ./tests

clean:
	@echo $(START)'Cleaning'$(END)
	rm -rf $(DISTPATH)

clear-cache:
	@echo $(START)'Clearing poetry cache'$(END)
	rm -rf $(POETRY_CACHE_DIR)

clean-all: clean
	@echo $(START)'Clean all work files'$(END)
	rm -rf ./.venv
