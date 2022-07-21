import os


class BaseConfig:
    TESTING = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "my_precious")
    RESTX_ERROR_404_HELP = False
{%- if cookiecutter.use_postgres == "yes" %}
    SQLALCHEMY_DATABASE_URI = os.environ.get("POSTGRES_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
{%- endif %}
{%- if cookiecutter.use_mongo == "yes" %}
    MONGO_URI = os.environ.get("MONGO_URI")
{%- endif %}
{%- if cookiecutter.use_celery == "yes" %}
    CELERY_BROKER_URL = os.environ.get(
        "CELERY_BROKER_URL"
    )
    CELERY_RESULT_BACKEND = os.environ.get(
        "CELERY_RESULT_BACKEND"
    )
    CELERY_TASK_DEFAULT_QUEUE = "{{cookiecutter.app_name}}_default_queue"

    CELERY_TASK_CREATE_MISSING_QUEUES = False
{%- endif %}


class DevelopmentConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    TESTING = True
{%- if cookiecutter.use_postgres == "yes" %}
    SQLALCHEMY_DATABASE_URI = os.environ.get("POSTGRES_TEST_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
{%- endif %}
{%- if cookiecutter.use_mongo == "yes" %}
    MONGO_URI = os.environ.get("MONGO_TEST_URI")
{%- endif %}


class ProductionConfig(BaseConfig):
    RESTX_ERROR_404_HELP = True
    SECRET_KEY = os.environ.get("SECRET_KEY")
