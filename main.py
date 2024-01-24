from fastapi import FastAPI, Request, HTTPException, Query
from fastapi.templating import Jinja2Templates
from motor.motor_asyncio import AsyncIOMotorClient
from fastapi.responses import HTMLResponse
from models import NFTMetadata
from typing import List

app = FastAPI()

# MongoDB Client
mongo_client = AsyncIOMotorClient("mongodb+srv://notpurf:<password>@worthlessgallery.kz3n2ux.mongodb.net/?retryWrites=true&w=majority")
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


@app.get("/nfts/info/{type}", response_class=HTMLResponse)
async def get_nft_info(request: Request, type: str, color: str = None):
    nfts = await db.worthlesscollection.find({"type": type}).to_list(None)  # Fetch NFTs of the specific type
    nft = nfts[0] if nfts else None  # Get the first NFT if the list is not empty
    info_dict = {
        "common": "Common NFTs are the most frequently found NFTs in our collection. Rate Limit of 1 transaction per second.",
        "un-common": "Un-common NFTs are less frequently found and have special features.",
        "rare": "Rare NFTs are hard to find and highly valuable.",
        "super-rare": "Super Rare: Rate limit of 6 transactions per second, burst to 12 transactions per second if overflow and NFT has not been traded or sent to another wallet in one (1) month.",
        "epic": "Epic: Rate limit of 10 transactions per second, burst to 20 transactions per second if overflow and NFT has not been traded or sent to another wallet in one (1) month.",
        "invisible": "Invisible NFTs have a special ability to become invisible.",
    }
    info = info_dict.get(type, "")
    template_name = f"{type}.html"
    return templates.TemplateResponse(template_name, {"request": request, "info": info, "nfts": nfts, "nft": nft, "color": color})

# shop all 
@app.get("/path/to/nfts", response_class=HTMLResponse)
async def get_nfts_page(request: Request, page: int = Query(1, ge=1)):
    skip = (page - 1) * 10
    nfts = await db.worthlesscollection.find({"attributes": {"$elemMatch": {"trait_type": "class", "value": "common"}}}).skip(skip).limit(10).to_list(None)
    return templates.TemplateResponse("nfts_fragment.html", {"request": request, "nfts": nfts})

@app.get("/path/to/uncommon_nfts", response_class=HTMLResponse)
async def get_uncommon_nfts_page(request: Request, page: int = Query(1, ge=1)):
    skip = (page - 1) * 10
    nfts = await db.worthlesscollection.find({"attributes": {"$elemMatch": {"trait_type": "class", "value": "un-common"}}}).skip(skip).limit(10).to_list(None)
    return templates.TemplateResponse("nfts_fragment.html", {"request": request, "nfts": nfts})

@app.get("/path/to/rare_nfts", response_class=HTMLResponse)
async def get_rare_nfts_page(request: Request, page: int = Query(1, ge=1)):
    skip = (page - 1) * 10
    nfts = await db.worthlesscollection.find({"attributes": {"$elemMatch": {"trait_type": "class", "value": "rare"}}}).skip(skip).limit(10).to_list(None)
    return templates.TemplateResponse("nfts_fragment.html", {"request": request, "nfts": nfts})

@app.get("/path/to/super_rare_nfts", response_class=HTMLResponse)
async def get_super_rare_nfts_page(request: Request, page: int = Query(1, ge=1)):
    skip = (page - 1) * 10
    nfts = await db.worthlesscollection.find({"attributes": {"$elemMatch": {"trait_type": "class", "value": "super-rare"}}}).skip(skip).limit(10).to_list(None)
    return templates.TemplateResponse("nfts_fragment.html", {"request": request, "nfts": nfts})

@app.get("/path/to/epic_nfts", response_class=HTMLResponse)
async def get_epic_nfts_page(request: Request, page: int = Query(1, ge=1)):
    skip = (page - 1) * 10
    nfts = await db.worthlesscollection.find({"attributes": {"$elemMatch": {"trait_type": "class", "value": "epic"}}}).skip(skip).limit(10).to_list(None)
    return templates.TemplateResponse("nfts_fragment.html", {"request": request, "nfts": nfts})

@app.get("/path/to/invisible_nfts", response_class=HTMLResponse)
async def get_invisible_nfts_page(request: Request, page: int = Query(1, ge=1)):
    skip = (page - 1) * 10
    nfts = await db.worthlesscollection.find({"attributes": {"$elemMatch": {"trait_type": "class", "value": "invisible"}}}).skip(skip).limit(10).to_list(None)
    return templates.TemplateResponse("nfts_fragment.html", {"request": request, "nfts": nfts})
