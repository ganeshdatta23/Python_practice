import pymongo.mongo_client import MongoClient
import pymongo.server_api import ServerApi

url = ""

client=MongoClient(url,server_api=ServerApi("1"))
db = client.todo_db