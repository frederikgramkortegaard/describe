# app.py

from module_bindings import detect, get_model
from fastapi import Request, FastAPI
from requests import JSONDecodeError
from fastapi import *

import uvicorn
import base64

app = FastAPI()


def decode_base64(base64_string) -> bytes:
    """Decodes a base64 string to bytes, adds padding if necessary"""

    return base64.b64decode(base64_string + "=" * (-len(base64_string) % 4))


@app.get("/")
async def run(info: Request):
    """Pipes a given base64 string through a Show-And-Tell Caption Generation model and
    returns the results as a JSON object.

    Args:
        info: A request object (a JSON request-body) with a field "base64" containing a base64-encoded image as a string.
    Returns:
        JSON object containing the detection results
    """

    try:
        req_info = await info.json()

    # @TODO : Change to specific exception type
    except:
        return {"STATUS": "ERROR", "error": "Invalid JSON"}

    # Validate input fields
    if "base64" not in req_info:
        return {"STATUS": "ERROR", "error": "base64 field is missing"}

    base64_str = req_info["base64"]

    # @TODO : Add logic to check the version number

    # @TODO : Add logic to run the version-specific code

    # Gets the model frm the module_bindings, this is cached so
    # it's not necessary to re-download the model every time
    model = get_model()

    if (results := detect(model, base64_str)) == None:
        return {"STATUS": "ERROR", "error": "Model failed to run"}

    try:
        # results_as_json = results.pandas().xyxy[0].to_json()
        pass

    except AttributeError or JSONDecodeError:
        return {
            "STATUS": "ERROR",
            "error": "Return value of model failed to convert to JSON",
        }

    return {"status": "SUCCESS", "metadata": "not implemented", "results": results}


if __name__ == "__main__":

    # @TODO : Get the port number and IP from environment variables

    uvicorn.run("app:app", host="127.0.0.1", port=5001)
