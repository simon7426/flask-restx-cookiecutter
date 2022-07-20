import os

from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo

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

    from {{cookiecutter.app_name}}.apis import api

    api.init_app(app)

    @app.shell_context_processor
    def ctx():  # pragma: no cover
        return {"app": app, "db": db}

    return app
