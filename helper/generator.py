from helper.database.db import get_database
import pandas as pd
from random import randint
import numpy as np
from datetime import datetime, timedelta, time
from helper.utils import doesExceed

DB = get_database()

# Get itinerary as DataFrame
def generate_itinerary(city, days, selected_categories):

  # Current Collection
  COLLECTION = DB[city]
  # Guard condition
  # If the number of places is more than avaiable dataset throw error
  # 1 : Get the number of availabe dataset in selected_categories
  # available_places = len(list(COLLECTION.find({'category' : {"$in" : selected_categories}})))
  # # 2 : Get # of places
  # wanted_places = days * 3
  # # 3 : Throw an error where # of places > # of availabe dataset
  # if (wanted_places > available_places) and selected_categories[0] != 'All':
  #   raise Exception(f"The destinations you wish to go are not enough for {days} days. Please select more categories or decrease the number of days")

  # Get the all city
  result = COLLECTION.find({})
  # Convert the result to Pandas
  df = pd.DataFrame(result)
  # Drop all Nan
  df = df[df['name_place'] != None]

  # Helper function
  def get_open_time(index):
    # The category of target place using random_index
    target_place_category = df.iloc[index]['category']
    # The open time of target place using random_index 
    target_place_open_time = df.iloc[index]['open(time)']
    # Extract hour and minute from string
    # The error might raise from here
    open_hour, open_minute = map(int, target_place_open_time.split(":"))

    return (open_hour, open_minute)
  
  def get_close_time(index):
    # The category of target place using random_index
    target_place_category = df.iloc[index]['category']
    # The open time of target place using random_index 
    target_place_close_time = df.iloc[index]['close(time)']
    # Extract hour and minute from string
    close_hour, close_minute = map(int, target_place_close_time.split(":"))

    return (close_hour, close_minute)

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
    # Track if current day is done or not
    currentDayDone = False
    while not currentDayDone:
      print(f'In Process... Day{current_day}')
      # random_index for place
      random_index = randint(0, len(df) - 1)

      target_place_category = df.iloc[random_index]['category']

      # If the target_place_category is 'All' category
      if selected_categories[0] == 'All':
        print(f"In All category")
        # if the place has time constraint
        if df.iloc[random_index]['open(time)'] and df.iloc[random_index]['close(time)']:
          print(f"in operation time condition")
          # open_time
          open_hour, open_minute = get_open_time(random_index)
          open_time = time(hour=open_hour, minute=open_minute, second=0, microsecond=0)
          # close_time
          close_hour, close_minute = get_close_time(random_index)
          close_time = time(hour=close_hour, minute=close_minute, second=0, microsecond=0)
          # Check if the current time is in the place's operation time
          while not (open_time <= current_time.time() < close_time) or (random_index in used_index):
            print(f"In Loop of All category operation time")
            print(f"Length of data : {len(df)}")
            random_index = randint(0, len(df) - 1)
            print(f"Done randoming index")
            # Update open_time and close_time
            # open_time
            print(f"Getting open hour")
            if df.iloc[random_index]['open(time)'] and df.iloc[random_index]['close(time)']:
              open_hour, open_minute = get_open_time(random_index)
              print(f"Got open hour {open_hour} {open_minute}")
              open_time = time(hour=open_hour, minute=open_minute, second=0, microsecond=0)
              # close_time
              print(f"Getting close hour")
              close_hour, close_minute = get_close_time(random_index)
              print(f"Got close hour {close_hour} {close_minute}")
              close_time = time(hour=close_hour, minute=close_minute, second=0, microsecond=0)
      else:
        print(f'In specific categories')
        # If the target place has time constraint
        if df.iloc[random_index]['open(time)'] and df.iloc[random_index]['close(time)']:
          print(f"in operation time condition")
          # open_time
          open_hour, open_minute = get_open_time(random_index)
          open_time = time(hour=open_hour, minute=open_minute, second=0, microsecond=0)
          # close_time
          close_hour, close_minute = get_close_time(random_index)
          close_time = time(hour=close_hour, minute=close_minute, second=0, microsecond=0)
          # random the index until the target_place has the related categories to selected_categories and in the operation time
          # This count will track the times the followgin while loop runs
          # If more than 100 it means it can't find the place so break the looop
          count = 0
          while (not df.iloc[random_index]['category'] in selected_categories) or (not open_time <= current_time.time() < close_time) or (random_index in used_index):
            count += 1

            if count > len(df):
              currentDayDone = True
              break

            print("In Loop of Specific category operation time")
            random_index = randint(0, len(df) - 1)
            print("Index :",random_index)
            print("current_time : ", current_time.time())
            # Update open_time and close_time
            # open_time
            if df.iloc[random_index]['open(time)'] and df.iloc[random_index]['close(time)']:
              open_hour, open_minute = get_open_time(random_index)
              open_time = time(hour=open_hour, minute=open_minute, second=0, microsecond=0)
              # close_time
              close_hour, close_minute = get_close_time(random_index)
              close_time = time(hour=close_hour, minute=close_minute, second=0, microsecond=0)
        # If the target place has no time constraint
        else:
          # Random the index until the target_place has the realted categories to selected_categories
          while (not df.iloc[random_index]['category']) or (random_index in used_index):
            print("In Loop of Specific category matching selected categories")
            random_index = randint(0, len(df) - 1)

      print("In process... Adding index to used_index list")
      # Adding this to used_index
      used_index.append(random_index)
      # random place
      random_place = df.iloc[random_index]
      # Serialize the randome place to wanted format
      serialized_place = {
        'name_place' : random_place['name_place'],
        'location' : random_place['location'],
        'open' : random_place['open(time)'],
        'close' : random_place['close(time)'],
        'description' : random_place['DCT'] if 'DCT' in random_place.keys() else '',
        'img_cover' : random_place['img_cover'] if 'img_cover' in random_place.keys() else '',
        'special_events' : random_place['special_events'].split(", "),
        'high_level_events' : random_place['high_level_events'].split(", ") if random_place['high_level_events'] != '""' else ""
      }
      # Add this random_place to current_places
      itinerary[f'Day{current_day + 1}'][current_time.strftime("%H:%M")] = serialized_place
      # Increase current time with transportation time and maximum_time_spending
      current_time = current_time + timedelta(minutes=30) + timedelta(minutes=int(random_place['maximum_time_spending(min)']))
      # Check if the current_time exceed end time
      # If yes, stop generating
      if current_time.time() >= end_time.time():
        currentDayDone = True
        break
  # return the itinerary
  return itinerary

# Get unqieu categories based on the city
async def get_categories(city):
  print(city)
  # Selected collection
  COLLECTION = DB[city]
  print(COLLECTION)
  # Fetch all data from the collection
  result = COLLECTION.find({})
  # Convert the result to dataFrame
  df = pd.DataFrame(result)
  print(df.columns)
  # Drop None value
  df = df[df['name_place'] != None]
  print(df)
  # Get the unique value from categories column
  unique_categories = list(np.unique(df['category']))
  print(unique_categories)
  # Create hash_table for categories and available places
  category_table = {}
  for category in unique_categories:
    query = list(COLLECTION.find({'category' : category}))
    # Create a key in the hash_table
    category_table[category] = 0
    # Replace the len in the current ky
    category_table[category] = len(query)
  # Return unique categories
  return category_table

