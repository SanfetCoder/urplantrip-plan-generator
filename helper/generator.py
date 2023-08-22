from database.db import get_database
import pandas as pd
from random import randint
import numpy as np
from datetime import datetime, timedelta

DB = get_database()

# Get itinerary as DataFrame
def get_itinerary(city, days):
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
    itinerary[f'Day{current_day + 1}'] = []
    for current_place in range(5):
      # random_index for place
      random_index = 0
      # Make sure it keeps randomizing the index til it is not the one in used_index
      while random_index in used_index:
        random_index = randint(0, len(df) - 1)
      # Adding this to used_index
      used_index.append(random_index)
      # random place
      random_place = df.iloc[random_index]
      # Add this random_place to current_places
      itinerary[f'Day{current_day + 1}'].append(random_place.to_dict())

  # return the itinerary
  return itinerary

print(get_itinerary('Korea_Seoul', 3))
