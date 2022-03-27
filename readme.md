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
```http
GET http://127.0.0.1:5000/find/ HTTP/1.1
Content-Type: application/json

{
  "url": "https://firebasestorage.googleapis.com/v0/b/alt=media"
}
```
### Add New Missing Person
```http
POST http://localhost:5000/find/ HTTP/1.1
Content-Type: application/json

{
  "url": "https://firebasestorage.googleapis.com/v0/b/alt=media",
  "face": "shopno"
}
```
### Delete Missing Person
```http
DELETE http://localhost:5000/find/ HTTP/1.1
Content-Type: application/json

{
  "face": "shopno"
}
```