from pydantic import BaseModel, HttpUrl
from typing import List

class Creator(BaseModel):
    address: str
    share: int

class File(BaseModel):
    uri: str
    type: str

class Attribute(BaseModel):
    trait_type: str
    value: str

class Properties(BaseModel):
    files: List[File]
    creators: List[Creator]

class Collection(BaseModel):
    name: str
    family: str

class NFTMetadata(BaseModel):
    name: str
    symbol: str
    description: str
    seller_fee_basis_points: str
    image: HttpUrl
    attributes: List[Attribute]
    collection: Collection
    properties: Properties
