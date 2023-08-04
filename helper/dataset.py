import os 
import pandas as pd


dataset_path = "/Users/sanphetlovestina/Desktop/urplantrip/apis/data-resources/"
# All files ignoring unrelated files
files = list(filter(lambda x : not x.startswith('.') , os.listdir(dataset_path)))

# Promp user's input
destination = input('Which city do you want to travel?')
duration = int(input("How long will you travel?"))
hasChild = input('Any child in your trip?').lower() == 'y'
hasOld = input('Any elder in your trip?').lower() == 'y'

# ====== Functions =========

# File path to be read by pandas
def file_path(filename):
  return dataset_path + filename
  