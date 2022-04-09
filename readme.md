# FACE RECOGNITION MISSING PERSON

## Project Setup
### Create Virtual Environment
```bash
python -m venv env
```
### Activate Virtual Environment
```bash
source env/Scripts/activate
```
### Install Dependencies
```bash
pip install cmake
pip install -r requirements.txt
```
### Run server
```bash
python server.py
```

## Usage Example
### Find Person
***
Request:
```http
GET http://127.0.0.1:5000/find/ HTTP/1.1
Content-Type: application/json

{
  "url": "https://firebasestorage.googleapis.com/v0/b/alt=media"
}
```
Response: FOUND
```http
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 24
Server: Werkzeug/2.0.3 Python/3.10.3
Date: Sun, 27 Mar 2022 04:40:17 GMT

{
  "found": "riad"
}
```
Response: NOT FOUND
```http
HTTP/1.0 404 NOT FOUND
Content-Type: application/json
Content-Length: 22
Server: Werkzeug/2.0.3 Python/3.10.3
Date: Sun, 27 Mar 2022 07:18:06 GMT

{
  "found": null,
  "error": "Face did not match"
}
```
Response: IMAGE NOT FOUND
```http
HTTP/1.0 404 NOT FOUND
Content-Type: application/json
Content-Length: 55
Server: Werkzeug/2.0.3 Python/3.10.3
Date: Sun, 27 Mar 2022 07:19:09 GMT

{
  "found": false,
  "error": "Image not found"
}
```
Response: INVALID ARGUMENTS
```http
HTTP/1.0 400 BAD REQUEST
Content-Type: application/json
Content-Length: 52
Server: Werkzeug/2.0.3 Python/3.10.3
Date: Sat, 09 Apr 2022 05:21:30 GMT

{
  "found": false,
  "error": "Invalid arguments"
}
```
### Add New Missing Person
***
Request:
```http
POST http://localhost:5000/find/ HTTP/1.1
Content-Type: application/json

{
  "url": "https://firebasestorage.googleapis.com/v0/b/alt=media",
  "face": "shopno"
}
```
Response: ADDED MISSING PERSON ENCODING
```http
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 27
Server: Werkzeug/2.0.3 Python/3.10.3
Date: Sun, 27 Mar 2022 04:38:00 GMT

{
  "successful": true
}
```
Response: ALREADY EXIST MISSING PERSON ENCODING
```http
HTTP/1.1 409 CONFLICT
Connection: close
Server: gunicorn
Date: Sat, 09 Apr 2022 05:16:32 GMT
Content-Type: application/json
Content-Length: 69
Via: 1.1 vegur

{
  "successful": false,
  "error": "Person with this ID already exists"
}
```
Response: FAILED ADDING MISSING PERSON ENCODING
```http
HTTP/1.0 500 INTERNAL SERVER ERROR
Content-Type: application/json
Content-Length: 55
Server: Werkzeug/2.0.3 Python/3.10.3
Date: Sun, 27 Mar 2022 07:19:09 GMT

{
  "successful": false,
  "error": "Unable to store on Database"
}
```
Response: IMAGE NOT FOUND
```http
HTTP/1.0 404 NOT FOUND
Content-Type: application/json
Content-Length: 55
Server: Werkzeug/2.0.3 Python/3.10.3
Date: Sun, 27 Mar 2022 07:19:09 GMT

{
  "successful": false,
  "error": "Image not found"
}
```
Response: INVALID ARGUMENTS
```http
HTTP/1.0 400 BAD REQUEST
Content-Type: application/json
Content-Length: 52
Server: Werkzeug/2.0.3 Python/3.10.3
Date: Sat, 09 Apr 2022 05:21:30 GMT

{
  "successful": false,
  "error": "Invalid arguments"
}
```
### Update Missing Person
***
Request:
```http
PATCH http://localhost:5000/find/ HTTP/1.1
Content-Type: application/json

{
  "url": "https://firebasestorage.googleapis.com/v0/b/alt=media",
  "face": "shopno"
}
```
Response: UPDATED MISSING PERSON ENCODING
```http
HTTP/1.0 204 NO CONTENT
Content-Type: application/json
Server: Werkzeug/2.0.3 Python/3.10.3
Date: Sun, 27 Mar 2022 04:35:54 GMT
```
Response: ALREADY DOES EXIST MISSING PERSON ENCODING
```http
HTTP/1.1 409 CONFLICT
Connection: close
Server: gunicorn
Date: Sat, 09 Apr 2022 05:16:32 GMT
Content-Type: application/json
Content-Length: 69
Via: 1.1 vegur

{
  "successful": false,
  "error": "Person with this ID does not exists"
}
```
Response: FAILED ADDING MISSING PERSON ENCODING
```http
HTTP/1.0 500 INTERNAL SERVER ERROR
Content-Type: application/json
Content-Length: 55
Server: Werkzeug/2.0.3 Python/3.10.3
Date: Sun, 27 Mar 2022 07:19:09 GMT

{
  "successful": false,
  "error": "Unable to store on Database"
}
```
Response: IMAGE NOT FOUND
```http
HTTP/1.0 404 NOT FOUND
Content-Type: application/json
Content-Length: 55
Server: Werkzeug/2.0.3 Python/3.10.3
Date: Sun, 27 Mar 2022 07:19:09 GMT

{
  "successful": false,
  "error": "Image not found"
}
```
Response: INVALID ARGUMENTS
```http
HTTP/1.0 400 BAD REQUEST
Content-Type: application/json
Content-Length: 52
Server: Werkzeug/2.0.3 Python/3.10.3
Date: Sat, 09 Apr 2022 05:21:30 GMT

{
  "successful": false,
  "error": "Invalid arguments"
}
```
### Delete Missing Person
***
Request:
```http
DELETE http://localhost:5000/find/ HTTP/1.1
Content-Type: application/json

{
  "face": "shopno"
}
```
Response: DELETED
```http
HTTP/1.0 204 NO CONTENT
Content-Type: application/json
Server: Werkzeug/2.0.3 Python/3.10.3
Date: Sun, 27 Mar 2022 04:35:54 GMT
```
Response: DELETE FAILED
```http
HTTP/1.0 500 INTERNAL SERVER ERROR
Content-Type: application/json
Content-Length: 55
Server: Werkzeug/2.0.3 Python/3.10.3
Date: Sun, 27 Mar 2022 07:19:09 GMT

{
  "successful": false,
  "error": "Unable to delete encoding"
}
```
Response: INVALID ARGUMENTS
```http
HTTP/1.0 400 BAD REQUEST
Content-Type: application/json
Content-Length: 52
Server: Werkzeug/2.0.3 Python/3.10.3
Date: Sat, 09 Apr 2022 05:21:30 GMT

{
  "successful": false,
  "error": "Invalid arguments"
}
```