import numpy
import pymongo
from pymongo import MongoClient

# CLIENT_URL ='mongodb://localhost:27017/'
CLIENT_URL ='mongodb+srv://<admin>:<ariana2838>@netjobs.jglqn.mongodb.net/faceRecognition?retryWrites=true&w=majority'

client = MongoClient(CLIENT_URL)
db = client.faceRecognition

def saveMissingPersonEncodings(encodeList, faceList):
  try:
    db.encodeList.insert_one({ "faceEncoding": list(encodeList[0]), "face": faceList })
    return True
  except Exception as e:
    print(e)
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
    print(f'ops {e}')
    return []

def deleteEncoding(face):
  try:
    db.encodeList.delete_one({ "face": face })
    return True
  except Exception as e:
    print(e)
    return False