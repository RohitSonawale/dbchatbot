
from motor.motor_asyncio import AsyncIOMotorClient
from src.configure.config_setting import setting
print("completed_________",setting.mongourl)
# Connect to MongoDB
client = AsyncIOMotorClient(setting.mongourl)
db = client.get_database()  # Automatically uses the 'kamdhenu' database
messages_collection = db.messages  # Collection to store chat messages
products_collection = db.products  # Collection to store product information
services_collection = db.services  # Collection to store service information
brands_collection = db.brands  # Collection to store brand information



