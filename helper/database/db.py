from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Configure dotenv
load_dotenv()

# Connect to MongoDB server
client = MongoClient(f'mongodb+srv://{os.getenv("USERNAME")}:{os.getenv("PASSWORD")}@urplantrip.pj6xxgf.mongodb.net/?retryWrites=true&w=majority')
# The name of database
DB = client['travel_places']

def get_database():
  return DB