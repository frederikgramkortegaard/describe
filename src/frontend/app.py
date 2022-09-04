
from flask import Flask
from flask import request
from flask import render_template
from flask import send_from_directory
import os
import glob
import sys
import argparse
import cv2
import binascii
import requests
import json
import base64


app = Flask("Flask Image Gallery")
app.config['IMAGE_EXTS'] = [".png", ".jpg", ".jpeg", ".gif", ".tiff"]


def encode(x):
    return binascii.hexlify(x.encode('utf-8')).decode()

def decode(x):
    return binascii.unhexlify(x.encode('utf-8')).decode()


@app.route('/')
def home():
    root_dir = app.config['ROOT_DIR']
    image_paths = []

    num = 0

    for root,dirs,files in os.walk(root_dir):
        for file in files:
    
            if num > 10:
                break
            else:
                num += 1


            if any(file.endswith(ext) for ext in app.config['IMAGE_EXTS']):
                image_paths.append(encode(os.path.join(root,file)))
    return render_template('index.html', paths=image_paths)


@app.route('/search', methods=['GET'])
def search():
    root_dir = app.config['ROOT_DIR']
    image_paths = []

    query = request.args.get('query')

    num = 0

    queries = requests.get('http://127.0.0.1:8000', json={"query": query}).json()


    total_data = {}

    for root,dirs,files in os.walk(root_dir):
        for file in files:
    
            if num > 10:
                break
            else:
                num += 1

            if any(file.endswith(ext) for ext in app.config['IMAGE_EXTS']):

                print(file)

                img = cv2.imread(os.path.join(root,file))
                jpg_img = cv2.imencode('.jpg', img)
                b64_string = base64.b64encode(jpg_img[1]).decode('utf-8')

                objects = requests.get('http://127.0.0.1:8001', json={"base64": b64_string}).json()
                caption = requests.get('http://127.0.0.1:8005', json={"base64": b64_string}).json()

                metadata = {
                    "objects": objects,
                    "queries": queries,
                    "caption": caption
                }

                similarity = requests.get('http://127.0.0.1:8003', json=metadata).json()["similarity"]

                if similarity <= 0.5:
                    break

                metadata["similarity"] = similarity
                total_data[os.path.join(root,file)] = metadata
                image_paths.append(encode(os.path.join(root,file)))

    json.dump(total_data, open("data.json", "w"))
    return render_template('index.html', paths=image_paths)



@app.route('/cdn/<path:filepath>')
def download_file(filepath):
    dir,filename = os.path.split(decode(filepath))
    return send_from_directory(dir, filename, as_attachment=False)


if __name__=="__main__":
    parser = argparse.ArgumentParser('Usage: %prog [options]')
    parser.add_argument('root_dir', help='Gallery root directory path')
    parser.add_argument('-l', '--listen', dest='host', default='127.0.0.1', \
                                    help='address to listen on [127.0.0.1]')
    parser.add_argument('-p', '--port', metavar='PORT', dest='port', type=int, \
                                default=5000, help='port to listen on [5000]')
    args = parser.parse_args()
    app.config['ROOT_DIR'] = args.root_dir
    app.run(host=args.host, port=args.port, debug=True)
