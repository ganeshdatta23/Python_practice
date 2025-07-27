from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def homepage():
    return {"message":"Jaya Guru Datta"}

@app.get("/companies")
async def companies():
    return {"message":"ganesh datta"}

