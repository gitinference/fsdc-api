from fastapi import FastAPI

from .routers import data

app = FastAPI()

app.include_router(data.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
