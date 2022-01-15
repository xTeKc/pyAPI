from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Welcome to my API!!"}

@app.get("/posts")
def get_posts():
    return {"data": "These are your posts"}