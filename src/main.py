from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from src.routers import data, files, graphs
from src.routers.research_bank import (
    subdisciplines,
    researchers,
    codebooks,
    datasets,
    research_entries,
)
from src.core.db import init_db

app = FastAPI()
init_db()


origins = [
    "http://localhost:3000",
    "http://192.168.50.24:5751",
    "fsdc.econlabs.net",
    "uprm.edu",
    "https://www.uprm.edu/foodsecuritydatacenter/series-de-tiempo/",
]

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
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}
