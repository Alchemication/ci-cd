"""
Example FastAPI app
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def read_main():
    """
    Example FastAPI route
    :return: dict
    """
    return {"msg": "Hello World"}
