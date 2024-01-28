.PHONY: init downgrade run


install:
	poetry install --no-root

init:
	poetry shell

migrate:
	poetry run python manage.py migrate

run:
	poetry run python manage.py runserver

test:
	poetry run python manage.py test