all: prod

prod:
	poetry config settings.virtualenvs.create true
	poetry config settings.virtualenvs.in-project false
	poetry install 

dev:
	poetry config settings.virtualenvs.create true
	poetry config settings.virtualenvs.in-project false
	poetry install --develop="pupy"
