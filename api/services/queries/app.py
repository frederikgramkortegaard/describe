# app.py

from module_bindings import *
from fastapi import Request, FastAPI
from requests import JSONDecodeError
from fastapi import *

import uvicorn

app = FastAPI()


@app.get("/")
async def run(info: Request):
    """Returns enriched metadata for a given input string, e.g. tokens, entities, etc.
    
    Args:
        info: A request object (a JSON request-body)
    
    Requires:
        query: A string containing the input string

    Returns:
        JSON object containing the enriched metadata
    """

    try:
        req_info = await info.json()

    # @TODO : Change to specific exception type
    except:
        return {"STATUS": "ERROR", "error": "Invalid JSON"}


    try:
        query = req_info['query']
        results = pipeline(query)
    except JSONDecodeError:
        return {"status": "ERROR", "error": "No query provided"}

    return {"status": "SUCCESS", "metadata": results}


if __name__ == "__main__":

    # @TODO : Get the port number and IP from environment variables

    uvicorn.run("app:app", host="127.0.0.1", port=5000)
