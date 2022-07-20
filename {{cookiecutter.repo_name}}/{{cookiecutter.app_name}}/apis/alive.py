from flask_restx import Namespace, Resource

alive_namespace = Namespace("alive")


@alive_namespace.route("", endpoint="alive")
class Alive(Resource):
    def get(self):
        response = {"message": "alive"}
        return response, 200
