import numpy as np
import base64
import cv2


def get_model():
    """Gets the pre-trained model from the module_bindings """
    return None


def detect(model, base64_str):
    """Runs the model on the given base64 string and returns the model result."""

    img = base64.b64decode(base64_str)
    npimg = np.fromstring(img, dtype=np.uint8)
    source = cv2.imdecode(npimg, 1)
    
    # results = model(source)

    return None
