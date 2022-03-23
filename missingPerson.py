import cv2
import numpy as np
import face_recognition
import os

from face_recognition.api import face_distance

# store images with their name as filename
# set the path as the name of the missing persons folder
path = 'MissingPersons'
images = []
missingPersons = []
missingPersonsList = os.listdir(path)

for missingPerson in missingPersonsList :
    curImg = cv2.imread(f'{path}/{missingPerson}')
    images.append(curImg)
    missingPersons.append(os.path.splitext(missingPerson)[0])
print(missingPersons)

# Run findEncodings function everytime a missing person
# is added to the database to save time
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    print(encodeList)
    return encodeList
 
 
encodeListKnown = findEncodings(images)
print('Encoding Complete')

# reported person folder contains the images of the person that are reported as found
def findMissingPerson(encodeListKnown):
    person = face_recognition.load_image_file(f'ReportedPersons/found1.jpg')
    person = cv2.cvtColor(person,cv2.COLOR_BGR2RGB)

    try:
        encodePerson = face_recognition.face_encodings(person)[0]

        comparedFace = face_recognition.compare_faces(encodeListKnown,encodePerson)
        faceDis = face_recognition.face_distance(encodeListKnown,encodePerson)
        matchIndex = np.argmin(faceDis)
        if comparedFace[matchIndex]:
            name = missingPersons[matchIndex].upper()
            print(name)
            return name
        else:
          print('Not Found')
          return False


    except IndexError as e:
        print(e)
        return e

findMissingPerson(encodeListKnown)