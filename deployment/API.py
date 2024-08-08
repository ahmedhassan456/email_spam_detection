from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def test(name:str):
    return {"name": name}