from fastapi import FastAPI, HTTPException
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
  try:
    unique_categories = await get_categories(city=city)
  except:
    raise HTTPException(status_code=400, detail="Fail")
  return unique_categories