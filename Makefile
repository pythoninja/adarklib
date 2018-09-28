# Test and build application

START="\n\n\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"
PYTHON_VERSION=3.7.0
PYTHON_BIN="${HOME}/.pyenv/versions/$(PYTHON_VERSION)/bin/python"
PYTHON_VENV="$(shell pwd)/.venv/bin/python"
POETRY_BIN="${HOME}/.pyenv/versions/$(PYTHON_VERSION)/bin/poetry"
DISTPATH="$(shell pwd)/dist"

.PHONY: test-ci

ready:
	$(PYTHON_BIN) -m pip install poetry; \
	$(POETRY_BIN) config settings.virtualenvs.in-project true || exit 1; \
	$(POETRY_BIN) install || exit 1; \

update:
	$(POETRY_BIN) update || exit 1

test:
	@echo $(START)'Running tests'$(END)
	$(PYTHON_VENV) -m unittest discover --verbose -s ./tests -t ./tests

test-ci:
	@echo $(START)'Running tests on CI'$(END)
	python -m unittest discover --verbose -s ./tests -t ./tests

clean:
	rm -rf $(DISTPATH)

clean-all: clean
	rm -rf ./.venv
