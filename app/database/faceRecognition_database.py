import os
import numpy
import pymongo
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

# CLIENT_URL ='mongodb://localhost:27017/'
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')
CLIENT_URL = f'mongodb+srv://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}?retryWrites=true&w=majority'

client = pymongo.MongoClient(CLIENT_URL, server_api=ServerApi('1'))
db = client.faceRecognition

def saveMissingPersonEncodings(encodeList, faceList):
  try:
    db.encodeList.insert_one({ "faceEncoding": list(encodeList[0]), "face": faceList })
    return True
  except Exception as e:
    print(e)
    return False

def updateMissingPersonEncodings(encodeList, faceList):
  try:
    db.encodeList.update_one({ "face": faceList },{ "$set": { "faceEncoding": list(encodeList[0]) } })
    return True
  except Exception as e:
    print(f'ops {e}')
    return False

def getMissingPersonEncodings():
  try:
    faceCursor = db.encodeList.aggregate([{
      "$group": {
        "_id": 'encodings',
        "knownEncodings": {
          "$push": "$faceEncoding"
        },
        "faceList": {
          "$push": "$face"
        }
      }
    }])
    if not faceCursor:
      return None
    for faceEncodings in faceCursor:
      knownEncodings = faceEncodings['knownEncodings']
      encoding = [ numpy.array(faceEncoding) for faceEncoding in knownEncodings]
      return {"encoding": encoding, "faces": faceEncodings['faceList']}
  except Exception as e:
    print(e)
    return []

def deleteEncoding(face):
  try:
    db.encodeList.delete_one({ "face": face })
    return True
  except Exception as e:
    print(e)
    return False

def getExistingMissingPersonEncoding(missingPersonId):
  isEncoded = db.encodeList.find_one({ 'face': missingPersonId })
  return isEncoded