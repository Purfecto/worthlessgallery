from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# MongoDB URI and credentials
uri = "mongodb+srv://notpurf:scissor@cluster0.giwgtxw.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri)

# Data to be inserted
worthlesspixel_data = {
    "name": "the worthless pixels invisible",
    "symbol": "WPIX",
    "description": "Yachts in Dubai Harbor at Sunrise",
    "seller_fee_basis_points": "500",
    "image": "https://mint-api.worthlesspixels.com/nftImages/dubaiyachtinharboratsunrise.png",
    "attributes": [
        {"trait_type": "guid", "value": "a11fc746606a464db1823d2fe59e90e8"},
        {"trait_type": "class", "value": "invisible"},
        {"trait_type": "week", "value": "1"},
        {"trait_type": "lucky_code", "value": "349892738102"}
    ],
    "collection": {
        "name": "worthless pixels v1",
        "family": "worthless pixels"
    },
    "properties": {
        "files": [
            {"uri": "808.png", "type": "image/png"},
            {"uri": "808.mp4", "type": "video/mp4"}
        ],
        "creators": [
            {"address": "8GhhyfrMfQEP2CyJcw6FUGxTJ3pDguguype8eAxADVL2", "share": 90},
            {"address": "narfn77NVRRfa4frg1KZykyFrJ1f9eMGnzXeMn2ja1X", "share": 5},
            {"address": "E3M4WNvfwdw2g5zHcqpivunf3DLM8boNMFMLPyS66nGh", "share": 5}
        ]
    }
}

# The rest of your script remains the same...

# The rest of your script remains the same...
# Specify the database and collection
db = client['worthlessdb']
collection = db['worthlesscollection']

# Insert the data into the collection
try:
    result = collection.insert_one(worthlesspixel_data)
    print(f"Data inserted with record id {result.inserted_id}")
except Exception as e:
    print(f"An error occurred: {e}")
