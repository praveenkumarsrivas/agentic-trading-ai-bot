from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI"}

@app.post("/upload")
def upload():
    return {"status": "file received"}
