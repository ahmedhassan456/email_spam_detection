from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def test(name:str):
    return {"name": name}


@app.get("/spam detection")
def spam_detection(email:str):
    return {"email": email}