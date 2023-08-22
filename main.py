from fastapi import FastAPI
from helper.generator import generate_itinerary, get_categories
# Create an app for this API
app = FastAPI()

# At root route
@app.get("/itinerary/{city}/{days}")
def get_itinerary(city, days):  
  itinerary = generate_itinerary(city=city, days=int(days))
  return itinerary

@app.get("/categories/{city}")
async def categories(city):
  unique_categories = await get_categories(city=city)
  return {
    "categories" : unique_categories
  }