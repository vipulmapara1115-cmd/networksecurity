from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://vipulmapara1115_db_user:seemad810@cluster0.e0lqdpx.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)