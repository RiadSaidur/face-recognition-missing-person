from flask import Flask, request
from flask_restful import Api, Resource

from database.db import deleteEncoding, getMissingPersonEncodings, saveMissingPersonEncodings
from services.faceRecognition import findEncodings, findMissingPerson

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
  
  def post(self):
    try:
      missingPersonURL = request.get_json()['url']
      missingPersonId = request.get_json()['face']
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
  
  def delete(self):
    face = request.get_json()['face']
    isDeleted = deleteEncoding(face)
    if isDeleted:
      return { "successful": True }, 204
    else:
      return { "successful": False, "error": "Unable to delete encoding" }, 500


api.add_resource(FaceRecognition, '/find/')

if __name__ == '__main__':
  app.run(debug=True)