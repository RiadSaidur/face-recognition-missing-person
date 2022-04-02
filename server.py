from flask import Flask
from flask_restful import Api

from app.routes.faceRecognition_routes import FaceRecognition

app = Flask(__name__)
api = Api(app)

api.add_resource(FaceRecognition, '/find/')