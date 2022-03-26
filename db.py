import numpy
import pymongo
from pymongo import MongoClient

CLIENT_URL ='mongodb://localhost:27017/'

client = MongoClient(CLIENT_URL)
db = client.faceRecognition

def saveMissingPersonEncodings(encodeList, faceList):
  try:
    db.encodeList.update_one({ "pk": "BASE" }, { "$push": { "knownEncodings": list(encodeList[0]), "faceList": faceList } }, upsert=True)
    return True
  except Exception as e:
    print(e)
    return False

def getMissingPersonEncodings():
  try:
    faceEncodings = db.encodeList.find_one({ "pk": "BASE" })
    if not faceEncodings:
      return None
    knownEncodings = faceEncodings['knownEncodings']
    encoding = [ numpy.array(faceEncoding) for faceEncoding in knownEncodings]
    return {"encoding": encoding, "faces": faceEncodings['faceList']}
  except Exception as e:
    print(e)
    return False