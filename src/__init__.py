from flask import Flask, jsonify
from flask_restx import Resource, Api


app = Flask(__name__)
api = Api(app)


class Ping(Resource):
    def get(self):
        return {'status': 'success', 'message': 'Urantia!'}


api.add_resource(Ping, '/ping')
