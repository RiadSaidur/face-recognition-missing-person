from urllib.error import HTTPError
from PIL import Image
from urllib.request import urlopen
import cv2
import numpy as np
import face_recognition

def getCvtColorImageFromURL(url):
  try:
    img = np.array(Image.open(urlopen(url)))
    return cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
  except HTTPError:
    return None

# Run findEncodings function everytime a missing person
# is added to the database to save time
def findEncodings(missingPersonsList):
  encodeList = []
  for missingPerson in missingPersonsList :
    img = getCvtColorImageFromURL(missingPerson)
    print(f'img {img}')
    if not img:
      return None
    encode = face_recognition.face_encodings(img)[0]
    encodeList.append(encode)

  return encodeList

# reported person folder contains the images of the person that are reported as found
def findMissingPerson(encodeListKnown, reportedPerson):
  try:
    person = getCvtColorImageFromURL(reportedPerson)
    if not person:
      raise FileNotFoundError
    encodePerson = face_recognition.face_encodings(person)[0]
    comparedFace = face_recognition.compare_faces(encodeListKnown['encoding'],encodePerson)
    faceDis = face_recognition.face_distance(encodeListKnown['encoding'],encodePerson)

    matchIndex = np.argmin(faceDis)
    if comparedFace[matchIndex]:
      name = encodeListKnown['faces'][matchIndex]
      return name
    else:
      return None

  except IndexError as e:
    print(e)
    return None