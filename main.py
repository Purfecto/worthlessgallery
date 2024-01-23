from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.responses import HTMLResponse
from models import NFTMetadata
from typing import List



app = FastAPI()

# MongoDB Client
mongo_client = AsyncIOMotorClient("mongodb+srv://notpurf:<PASSWORD>@cluster0.giwgtxw.mongodb.net/?retryWrites=true&w=majority")
db = mongo_client.worthlessdb

# Jinja2 Templates
templates = Jinja2Templates(directory="templates")

# Function to fetch all NFTs from MongoDB
async def get_all_nfts():
    nfts = await db.worthlesscollection.find().to_list(None)
    return nfts

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    nfts = await get_all_nfts()  # Fetch NFTs from MongoDB
    return templates.TemplateResponse("index.html", {"request": request, "nfts": nfts})


@app.get("/api/nfts", response_model=List[NFTMetadata])
async def get_nfts():
    return await get_all_nfts()

