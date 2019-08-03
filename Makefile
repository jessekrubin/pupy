all: say_hello generate

say_hello:
	@echo "Hello World"

generate:
	@echo "Creating empty text files..."
	touch file-{1..10}.txt

dev:
	poetry config settings.virtualenvs.create true
	poetry config settings.virtualenvs.in-project false
	poetry install --develop="pupy"
