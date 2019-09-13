all: prod
.PHONY: stub

prod:
	poetry config settings.virtualenvs.create true
	poetry config settings.virtualenvs.in-project false
	poetry install 

dev:
	poetry config settings.virtualenvs.create true
	poetry config settings.virtualenvs.in-project false
	poetry install --develop="pupy"

test:
	poetry run pytest

fmt:
	black pupy/*.py
	black pupy/*.pyi
	isort -sl -y pupy/*.py
	black tests/*.py
	isort -sl -y tests/*.py

stub:
	poetry run python manage.py mkstubs

clean:
	rm pupy/*.pyi

check:
	poetry run mypy --strict pupy


