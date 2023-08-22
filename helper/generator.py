from database.db import get_database
import pandas as pd

DB = get_database()

# Get itinerary as DataFrame
def get_itinerary(city):
  # Current Collection
  COLLECTION = DB[city]
  # Get the all city
  result = COLLECTION.find({})
  # Convert the result to Pandas
  df = pd.DataFrame(result)
  # Drop all Nan
  df = df.dropna()
  # Return the dataframe
  return df

print(get_itinerary('Korea_Seoul'))