# app.py

from module_bindings import *
from fastapi import Request, FastAPI
from requests import JSONDecodeError
from fastapi import *

import uvicorn
import json

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
    except Exception as e:
        return {"STATUS": "ERROR", "error": "Invalid JSON"}

    try:
        query = req_info['query']
    except JSONDecodeError:
        return {"status": "ERROR", "error": "No query provided"}

    results = pipeline(query)
    return {"status": "SUCCESS", "metadata": results}


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

    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
