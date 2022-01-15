from fastapi import FastAPI
from fastapi.params import Body

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to my API!!"}

@app.get("/posts")
def get_posts():
    return {"data": "These are your posts"}

@app.post("/createpost")
def create_post(payload: dict = Body(...)):
    print(payload)
    return {"new_post": f"title: {payload['title']} content {payload}['content']"}