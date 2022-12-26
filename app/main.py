from fastapi import FastAPI


app = FastAPI()



@app.get("/home")
@app.get("/")
async def  home():
    return {
        "API is online"}