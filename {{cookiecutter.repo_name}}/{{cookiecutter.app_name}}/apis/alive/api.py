from flask_restx import Namespace, Resource
{%- if cookiecutter.use_celery == "yes" %}
from {{cookiecutter.app_name}}.apis.alive.tasks import test_celery
{%- endif %}

alive_namespace = Namespace("alive")


@alive_namespace.route("", endpoint="alive")
class Alive(Resource):
    def get(self):
        response = {"message": "alive"}
        return response, 200
{%- if cookiecutter.use_celery == "yes" %}


@alive_namespace.route("/celery", endpoint="alive-celery")
class CeleryAlive(Resource):
    @alive_namespace.response(200, "Alive Celery")
    def get(self):
        task_id = test_celery.apply_async(args=[10, 5])
        response = {"message": "celeryalive", "task_id": str(task_id)}
        return response, 200
{%- endif %}
