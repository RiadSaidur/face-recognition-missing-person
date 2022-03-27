from flask import request
from flask_restful import Resource

from database.faceRecognition_database import deleteEncoding, getMissingPersonEncodings, saveMissingPersonEncodings
from services.faceRecognition_services import findEncodings, findMissingPerson


class FaceRecognition(Resource):
  def get(self):
    try:
      reportedPersonURL = request.get_json()['url']
      encodedList = getMissingPersonEncodings()
      isFound = findMissingPerson(encodedList, reportedPersonURL)
      if isFound == None:
        return { "found": isFound }, 404
      else:
        return { "found": isFound }, 200
    except FileNotFoundError:
      return { "found": False, "error": "Image not found" }, 404
  
  def post(self):
    try:
      missingPersonURL = request.get_json()['url']
      missingPersonId = request.get_json()['face']
      images = [missingPersonURL]
      print(f'encoding started {missingPersonURL}')
      encodeList = findEncodings(images)
      if not encodeList:
        return { "successful": False, "error": "Image not found" }, 404
      isSaved = saveMissingPersonEncodings(encodeList, missingPersonId)
      if isSaved:
        return { "successful": True }, 201
      return { "successful": False, "error": "Unable to store on Database" }, 500
    except KeyError:
      return { "successful": False, "error": "Invalid arguments" }, 500
  
  def delete(self):
    try:
      face = request.get_json()['face']
      isDeleted = deleteEncoding(face)
      if isDeleted:
        return { "successful": True }, 204
      else:
        return { "successful": False, "error": "Unable to delete encoding" }, 500
    except KeyError:
      return { "successful": False, "error": "Invalid arguments" }, 500
      