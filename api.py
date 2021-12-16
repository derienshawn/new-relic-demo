from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"data": "test"}

@app.get("/home")
def home():
    return "Hello world"

@app.get("/numbers")
def home():
    return "33434958469"