.PHONY: install
install:
	@poetry install --no-root --with=dev

.PHONY: repl
repl:
	@poetry run ipython

.PHONY: format
format:
	@poetry run black --color --target-version=py312 src