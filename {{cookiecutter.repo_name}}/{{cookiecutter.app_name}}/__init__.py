import os

from flask import Flask
{%- if cookiecutter.use_cors == "yes" %}
from flask_cors import CORS
{%- endif %}
{%- if cookiecutter.use_postgres == "yes" %}
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
{%- endif %}
{%- if cookiecutter.use_mongo == "yes" %}
from flask_pymongo import PyMongo
{%- endif %}
{%- if cookiecutter.use_celery == "yes" %}
from flask_celeryext import FlaskCeleryExt
from {{cookiecutter.app_name}}.celery_utils import make_celery
{%- endif %}


{%- if cookiecutter.use_cors == "yes" %}
cors = CORS()
{%- endif %}
{%- if cookiecutter.use_postgres == "yes" %}
db = SQLAlchemy()
migrate = Migrate()
{%- endif %}
{%- if cookiecutter.use_mongo == "yes" %}
mongo = PyMongo()
{%- endif %}
{%- if cookiecutter.use_celery == "yes" %}
ext_celery = FlaskCeleryExt(create_celery_app=make_celery)
{%- endif %}


def create_app():
    app = Flask(__name__)
    app_settings = os.environ.get("APP_SETTINGS", "{{cookiecutter.app_name}}.config.DevelopmentConfig")
    app.config.from_object(app_settings)


{%- if cookiecutter.use_cors == "yes" %}
    cors.init_app(app)
{%- endif %}
{%- if cookiecutter.use_postgres == "yes" %}
    db.init_app(app)
    migrate.init_app(app, db)
{%- endif %}
{%- if cookiecutter.use_mongo == "yes" %}
    mongo.init_app(app)
{%- endif %}
{%- if cookiecutter.use_celery == "yes" %}
    ext_celery.init_app(app)
{%- endif %}

    from {{cookiecutter.app_name}}.apis import api

    api.init_app(app)

    @app.shell_context_processor
    def ctx():  # pragma: no cover
{%- if cookiecutter.use_postgres == "yes" %}
        return {"app": app, "db": db}
{%- else %}
        return {"app": app}
{%- endif %}

    return app
