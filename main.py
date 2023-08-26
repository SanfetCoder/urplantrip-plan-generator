from fastapi import FastAPI, HTTPException
from helper.generator import generate_itinerary, get_categories

# Create an app for this API
app = FastAPI()

# At root route
@app.get("/itinerary/{city}/{days}/{categories}")
def get_itinerary(city, days, categories):
  # Convert the requestedc categories to Python list
  cat_list = categories.split(',') if ',' in categories else [categories]
  try:
    itinerary = generate_itinerary(city=city, days=int(days), selected_categories=cat_list)
    return itinerary
  except Exception as e:
    return HTTPException(status_code = 400, detail=str(e))

@app.get("/categories/{city}")
async def categories(city):
  try:
    unique_categories = await get_categories(city=city)
    return unique_categories
  except:
    return HTTPException(status_code=400, detail="Fail")