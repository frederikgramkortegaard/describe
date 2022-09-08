# app.py

from fastapi import Request, FastAPI
from fastapi import *

from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.applications.vgg16 import preprocess_input
from collections import OrderedDict
from module_bindings import *
from keras import models
from PIL import Image

import io
import cv2
import json
import base64
import uvicorn
import numpy as np

app = FastAPI()

def decode_base64(base64_string) -> bytes:
    """Decodes a base64 string to bytes, adds padding if necessary"""

    return base64.b64decode(base64_string + "=" * (-len(base64_string) % 4))


@app.get("/")
async def run(info: Request):
    """Pipes a given base64 string through a YOLOv5 object detectio model and
    returns the results as a JSON object.

    Args:
        info: A request object (a JSON request-body) with a field "base64" containing a base64-encoded image as a string.
    Returns:
        JSON object containing the detection results
    """

    try:
        req_info = await info.json()
    
    except Exception as e:
        return {"STATUS": "ERROR", "error": "Invalid JSON"}

    # Validate input fields
    if "base64" not in req_info:
        return {"STATUS": "ERROR", "error": "base64 field is missing"}

    base64_str = req_info["base64"]

    return {"STATUS": "ERROR", "error": "issue on laptop, tokenizer doesnt have attribute analyzer"}

    # convert base64 to cv2 image
    img = decode_base64(base64_str)
    img = Image.open(io.BytesIO(img))
    model,tokenizer,xception_model = get_model()
    result = generate_desc(model, tokenizer, xception_model,img)

    return {"status": "SUCCESS", "caption":  result}


if __name__ == "__main__":

    # @TODO : Get the port number and IP from environment variables

    from fastapi.middleware.cors import CORSMiddleware
    

    origins = [
    "http://127.0.0.1:5004"
    ]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    uvicorn.run("app:app", host="127.0.0.1", port=8005, reload=True)

