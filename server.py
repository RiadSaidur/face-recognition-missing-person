from flask import Flask, request
from flask_restful import Api, Resource
from db import getMissingPersonEncodings, saveMissingPersonEncodings

from faceRecognition import findEncodings, findMissingPerson

app = Flask(__name__)
api = Api(app)

class FaceRecognition(Resource):
  def get(self):
    reportedPersonURL = request.get_json()['url']
    encodedList = getMissingPersonEncodings()
    isFound = findMissingPerson(encodedList, reportedPersonURL)
    if isFound == None:
      return { "found": isFound }, 404
    else:
      return { "found": isFound }, 200

class Encode(Resource):
  def post(self):
    try:
      missingPersonURL = request.get_json()['url']
      missingPersonId = request.get_json()['mid']
      images = [missingPersonURL]
      print(f'encoding started {missingPersonURL}')
      encodeList = findEncodings(images)
      if encodeList:
        isSaved = saveMissingPersonEncodings(encodeList, missingPersonId)
        if isSaved:
          return { "successful": True }, 201
      return { "successful": False, "error": "Unable to store on Database" }, 500
    except KeyError:
      return { "successful": False, "error": "Invalid arguments" }, 500

api.add_resource(FaceRecognition, '/find/')
api.add_resource(Encode, '/encode/')

if __name__ == '__main__':
  app.run(debug=True)