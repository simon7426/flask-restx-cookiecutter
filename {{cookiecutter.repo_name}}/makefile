HOST ?= 0.0.0.0
PORT ?= 8000

server:
	FLASK_ENV=development poetry run python manage.py run -p $(PORT) -h $(HOST)
{%- if cookiecutter.use_celery == "yes" %}

worker:
	poetry run python manage.py celery_worker
{%- endif %}

test:
	poetry run pytest

format:
	poetry run black {{cookiecutter.app_name}}
	poetry run isort {{cookiecutter.app_name}} --profile black
	poetry run black manage.py
	poetry run isort manage.py --profile black

coverage:
	poetry run coverage run -m pytest
	poetry run coverage report -m

lint:
	poetry run flake8 {{cookiecutter.app_name}}
	poetry run black {{cookiecutter.app_name}} --check --quiet
	poetry run isort {{cookiecutter.app_name}} --profile black --check-only
	poetry run flake8 manage.py
	poetry run black manage.py --check --quiet
	poetry run isort manage.py --profile black --check-only

vulnerabilities:
	poetry run bandit -r {{cookiecutter.app_name}}
	poetry run safety check --short-report

tox:
	poetry run tox
