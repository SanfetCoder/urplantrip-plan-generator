from fastapi import FastAPI, HTTPException
from helper.generator import generate_itinerary, get_categories

# Create an app for this API
app = FastAPI()

# At root route
@app.get("/itinerary/{city}/{days}/{categories}")
def get_itinerary(city, days, categories):
  # Convert the requestedc categories to Python list
  cat_list = categories.split(',') if ',' in categories else [categories]
  itinerary = generate_itinerary(city=city, days=int(days), selected_categories=categories)
  return itinerary

@app.get("/categories/{city}")
async def categories(city):
  try:
    unique_categories = await get_categories(city=city)
  except:
    raise HTTPException(status_code=400, detail="Fail")
  return unique_categories