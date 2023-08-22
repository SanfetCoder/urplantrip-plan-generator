from pymongo import MongoClient
from dotenv import load_dotenv
import pandas as pd
import os

# Configure dotenv
load_dotenv()

# Connect to MongoDB server
client = MongoClient(f'mongodb+srv://{os.getenv("USERNAME")}:{os.getenv("PASSWORD")}@urplantrip.pj6xxgf.mongodb.net/?retryWrites=true&w=majority')
# The name of database
DB = client['travel_places']

# Get itinerary as DataFrame
def get_itinerary(city):
  # Current Collection
  COLLECTION = DB[city]
  # Get the all city
  result = COLLECTION.find({})
  # Convert the result to Pandas
  df = pd.DataFrame(result)
  # Return the dataframe
  return df

print(get_itinerary('Korea_Seoul'))