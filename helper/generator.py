import os 
import pandas as pd
from travel_categories import categories
from random import randint
from enum import Enum

# ====== Functions =========

# File path to be read by pandas
def file_path(filename):
  return dataset_path + filename

# =========> Algorithm part <=========

dataset_path = "/Users/sanphetlovestina/Desktop/urplantrip/apis/data_resources/"
# All files ignoring unrelated files
files = list(filter(lambda x : not x.startswith('.') , os.listdir(dataset_path)))
# Korea_seoul dataset
korea_seoul = pd.DataFrame(pd.read_csv(file_path(files[0])))
# drop NaN Value
korea_seoul = korea_seoul.dropna(subset=['Kid_friendly','Old_Can_Walk'])

# Enum of column
from enum import Enum

class Columns(Enum):
  country = "country"
  area = "area"
  name_place = "name_place"
  location = "location"
  link_location = "link_location"
  lat_long = "lat_long"
  open_time = "open_time"
  close_time = "close_time"
  day_close = "day_close"
  best_hour = "best_hour"
  min_time_spending = "min_time_spending"
  max_time_spending = "max_time_spending"
  best_time_to_go = "best_time_to_go"
  month = "month"
  best_month = "best_month"
  special_events = "special_events"
  category = "category"
  suitable_to_go_with = "suitable_to_go_with"
  Kid_friendly = "Kid_friendly"
  Old_Can_Walk = "Old_Can_Walk"
  fee_USD = "fee_USD"

# Promp user's input
destination = input('Which city do you want to travel?')
duration = int(input("How long will you travel?"))
has_child = input('Any child in your trip?').lower() == 'y'
has_old = input('Any elder in your trip?').lower() == 'y'

# Change from Y and N to True and False
korea_seoul[Columns.Kid_friendly.value] = korea_seoul[Columns.Kid_friendly.value].apply(lambda value : value.lower() == 'y')
korea_seoul[Columns.Old_Can_Walk.value] = korea_seoul[Columns.Old_Can_Walk.value].apply(lambda value : value.lower() == 'y')

# Filter out places according to has_child and has_old
korea_seoul = korea_seoul[korea_seoul[Columns.Kid_friendly.value] == has_child]
korea_seoul = korea_seoul[korea_seoul[Columns.Old_Can_Walk.value] == has_old]

# Display available categories
available_categories = list(korea_seoul[Columns.category.value])
