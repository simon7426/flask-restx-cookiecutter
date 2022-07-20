from flask_restx import Api

from {{cookiecutter.app_name}}.apis.alive import alive_namespace

api = Api(version="1.0", title="{{cookiecutter.repo_name}} APIs", doc="/docs")

api.add_namespace(alive_namespace, path="/alive")

