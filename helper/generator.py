from helper.database.db import get_database
import pandas as pd
from random import randint
import numpy as np
from datetime import datetime, timedelta
from helper.utils import doesExceed

DB = get_database()

# Get itinerary as DataFrame
def generate_itinerary(city, days):
  # Current Collection
  COLLECTION = DB[city]
  # Get the all city
  result = COLLECTION.find({})
  # Convert the result to Pandas
  df = pd.DataFrame(result)
  # Drop all Nan
  df = df.dropna()

  # Itinerary
  itinerary = {}
  # The indexing of places that have been already used
  used_index = []

  # adding places for each day
  for current_day in range(days):
    # Start time of the itinerary
    start_time = datetime(2023, 8, 1, 9, 0)
    # End time of the itinerary
    end_time = datetime(2023, 8, 1, 19, 0)
    # Current time for each place
    current_time = start_time
    # Create empty array for current day in the itinerary
    itinerary[f'Day{current_day + 1}'] = {}
    for current_place in range(5):
      # random_index for place
      random_index = randint(0, len(df) - 1)
      # Make sure it keeps randomizing the index til it is not the one in used_index
      while (random_index in used_index):
        random_index = randint(0, len(df) - 1)
      # Adding this to used_index
      used_index.append(random_index)
      # random place
      random_place = df.iloc[random_index]
      # Serialize the randome place to wanted format
      serialized_place = {
        'name_place' : random_place['name_place'],
        'location' : random_place['location'],
        'open' : random_place['open(time)'],
        'close' : random_place['close(time)']
      }
      # Add this random_place to current_places
      itinerary[f'Day{current_day + 1}'][current_time.strftime("%H:%M")] = serialized_place
      # Increase current time with transportation time and maximum_time_spending
      current_time = current_time + timedelta(minutes=30) + timedelta(minutes=int(random_place['maximum_time_spending(min)']))

  # return the itinerary
  return itinerary

# Get unqieu categories based on the city
async def get_categories(city):
  # Selected collection
  COLLECTION = DB[city]
  # Fetch all data from the collection
  result = COLLECTION.find({})
  # Convert the result to dataFrame
  df = pd.DataFrame(result)
  # Drop None value
  df = df.dropna()
  # Get the unique value from categories column
  unique_categories = list(np.unique(df['category']))
  # Return unique categories
  return unique_categories
