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
    """This endpoint is the entrypoint of the Search API.

    Args:
        info (Request): A request object

    Requires:
        info["query"] (str): A string representing the search query
        info["images"] (list): A list of base64 encoded images
        info["images"]["id"] (str): A string representing the image id

    Returns:
        A sorted JSON Object of image ids, metadata and similarity scores
    """

    return {"status": "SUCCESS", "metadata": ""}


if __name__ == "__main__":

    # @TODO : Get the port number and IP from environment variables

    uvicorn.run("app:app", host="127.0.0.1", port=5000)
