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
Response:
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
Response:
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
Response:
```http
HTTP/1.0 204 NO CONTENT
Content-Type: application/json
Server: Werkzeug/2.0.3 Python/3.10.3
Date: Sun, 27 Mar 2022 04:35:54 GMT
```