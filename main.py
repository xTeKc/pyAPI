from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/users/me")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}