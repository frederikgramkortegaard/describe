# app.py

from fastapi import Request, FastAPI
from fastapi import *

from nltk.data import find
word2vec_sample = str(find('models/word2vec_sample/pruned.word2vec.txt'))
model = gensim.models.KeyedVectors.load_word2vec_format(word2vec_sample, binary=False)

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
        objects = req_info['objects']
        caption = req_info['caption']
        queries = req_info['queries']

    except JSONDecodeError:
        return {"status": "ERROR", "error": "Invalid metadata provided"}

    # Caption Similarity
    sim = sum([model.similarity(c,q) for (c,q) in zip(caption.split(' '), queries["query"].split(' '))]) / len(caption)
    
    # Object Similarity
    #...


    return {"status": "SUCCESS", "similarity": sim}


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

    uvicorn.run("app:app", host="127.0.0.1", port=8003, reload=True)
