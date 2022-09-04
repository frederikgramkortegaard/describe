# app.py

import requests
import base64
import json
import cv2

img = cv2.imread('image.jpg')
jpg_img = cv2.imencode('.jpg', img)
b64_string = base64.b64encode(jpg_img[1]).decode('utf-8')

queries = requests.get('http://127.0.0.1:8000', json={"query": "Trumpet"}).json()
objects = requests.get('http://127.0.0.1:8001', json={"base64": b64_string}).json()
caption = requests.get('http://127.0.0.1:8002', json={"base64": b64_string}).json()

metadata = {
    "objects": objects,
    "queries": queries,
    "caption": caption
}

json.dump(metadata, open("test.json", 'w'), indent=4)
