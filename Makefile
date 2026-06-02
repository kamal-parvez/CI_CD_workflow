.PHONY: install lint format test check run

install:
	pip install -r requirements-dev.txt

lint:
	ruff check .
	ruff format --check .

format:
	ruff check . --fix
	ruff format .

test:
	pytest --cov=app --cov-report=term-missing

check: lint test

run:
	uvicorn app.main:app --reload