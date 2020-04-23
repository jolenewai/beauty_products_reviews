import pymongo
import os
from dotenv import load_dotenv
load_dotenv()

MONGO_URI = os.environ.get('MONGO_URI')

def get_client():
    # create a mongo client
    client = pymongo.MongoClient(MONGO_URI)
    return client
