from {{cookiecutter.app_name}} import create_app
{%- if cookiecutter.use_celery == "yes" %}
from {{cookiecutter.app_name}} import ext_celery
{%- endif %}

app = create_app()
{%- if cookiecutter.use_celery == "yes" %}
celery = ext_celery.celery
{%- endif %}
