import os

from flask import Flask, jsonify
from flask_restx import Resource, Api


app = Flask(__name__)

api = Api(app)

app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)


class Ping(Resource):
    def get(self):
        return {'status': 'success', 'message': 'Urantia!'}


api.add_resource(Ping, '/ping')
