from flask import request
from flask_restful import Resource

from app.database.faceRecognition_database import deleteEncoding, getMissingPersonEncodings, saveMissingPersonEncodings, updateMissingPersonEncodings
from app.services.faceRecognition_services import doesPersonExists, findEncodings, findMissingPerson


class FaceRecognition(Resource):
  def get(self):
    try:
      reportedPersonURL = request.args.get('url')
      encodedList = getMissingPersonEncodings()
      isFound = findMissingPerson(encodedList, reportedPersonURL)
      if isFound == None:
        return { "found": isFound, "error": "Face did not match" }, 404
      else:
        return { "found": isFound }, 200
    except FileNotFoundError:
      return { "found": False, "error": "Image not found" }, 404
    except KeyError:
      return { "found": False, "error": "Invalid arguments" }, 400
    except TypeError:
      return { "found": False, "error": "url argument required" }, 400
  
  def post(self):
    try:
      missingPersonURL = request.get_json()['url']
      missingPersonId = request.get_json()['face']
      doesExist = doesPersonExists(missingPersonId)
      if doesExist:
        return { "successful": False, "error": "Person with this ID already exists" }, 409
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
      return { "successful": False, "error": "Invalid arguments" }, 400
    except FileNotFoundError:
      return { "successful": False, "error": "Image not found" }, 404
  
  def patch(self):
    try:
      missingPersonURL = request.get_json()['url']
      missingPersonId = request.get_json()['face']
      doesExist = doesPersonExists(missingPersonId)
      if not doesExist:
        return { "successful": False, "error": "Person with this ID does not exists" }, 409
      images = [missingPersonURL]
      print(f'encoding started {missingPersonURL}')
      encodeList = findEncodings(images)
      if not encodeList:
        return { "successful": False, "error": "Image not found" }, 404
      isSaved = updateMissingPersonEncodings(encodeList, missingPersonId)
      if isSaved:
        return { "successful": True }, 204
      return { "successful": False, "error": "Unable to store on Database" }, 500
    except KeyError:
      return { "successful": False, "error": "Invalid arguments" }, 400
    except FileNotFoundError:
      return { "successful": False, "error": "Image not found" }, 404

  def delete(self):
    try:
      face = request.get_json()['face']
      isDeleted = deleteEncoding(face)
      if isDeleted:
        return { "successful": True }, 204
      else:
        return { "successful": False, "error": "Unable to delete encoding" }, 500
    except KeyError:
      return { "successful": False, "error": "Invalid arguments" }, 400
      