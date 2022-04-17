from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from app.routes.faceRecognition_routes import FaceRecognition

app = Flask(__name__)
CORS(app)
api = Api(app)

api.add_resource(FaceRecognition, '/find/')