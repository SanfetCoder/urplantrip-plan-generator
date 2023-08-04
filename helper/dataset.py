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
from enum import Enum, auto

class Categories(Enum):
  country = auto()
  area = auto()
  name_place = auto()
  location = auto()
  link_location = auto()
  lat_long = auto()
  open_time = auto()
  close_time = auto()
  day_close = auto()
  best_hour = auto()
  min_time_spending = auto()
  max_time_spending = auto()
  best_time_to_go = auto()
  month = auto()
  best_month = auto()
  special_events = auto()
  category = auto()
  suitable_to_go_with = auto()
  Kid_friendly = auto()
  Old_Can_Walk = auto()
  fee_USD = auto()

# # Promp user's input
# destination = input('Which city do you want to travel?')
# duration = int(input("How long will you travel?"))
# has_child = input('Any child in your trip?').lower() == 'y'
# has_old = input('Any elder in your trip?').lower() == 'y'
# #  Random 5 categories
# selected_categories = [categories[randint(0, len(categories) -1)] for _ in range(5)]

# Filter out places according to has_child and has_old
# korea_seoul[]

print(korea_seoul)
