import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.core.db import init_db
from src.routers import data, files, graphs
from src.routers.research_bank import (
    codebooks,
    datasets,
    research_entries,
    researchers,
    subdisciplines,
)

load_dotenv()


app = FastAPI()


origins = [
    "http://localhost:3000",
    "http://192.168.50.24:5751",
    "https://fsdc.econlabs.net",
    "https://fsdc-webapp.econlabs.net",
    "https://uprm.edu",
    "https://www.uprm.edu/foodsecuritydatacenter/series-de-tiempo/",
]

if os.getenv("DEV", "True").lower() == "true":
    origins = ["*"]


app.include_router(data.router)
app.include_router(files.router)
app.include_router(graphs.router)
app.include_router(subdisciplines.router)
app.include_router(researchers.router)
app.include_router(codebooks.router)
app.include_router(datasets.router)
app.include_router(research_entries.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["DELETE", "GET", "POST", "PUT"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
