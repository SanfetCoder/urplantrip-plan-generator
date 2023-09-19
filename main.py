from fastapi import FastAPI, HTTPException
from helper.generator import generate_itinerary, get_categories
from fastapi.middleware.cors import CORSMiddleware
import traceback

# Create an app for this API
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with the list of allowed origins (domains)
    allow_credentials=True,
    allow_methods=["*"],  # Replace with the HTTP methods you want to allow
    allow_headers=["*"],  # Replace with the HTTP headers you want to allow
)

# At root route
@app.get("/itinerary/{city}/{days}/{categories}")
def get_itinerary(city, days, categories):
  # Convert the requestedc categories to Python list
  cat_list = categories.split(',') if ',' in categories else [categories]
  try:
    itinerary = generate_itinerary(city=city, days=int(days), selected_categories=cat_list)
    return itinerary
  except Exception as e:
    return HTTPException(status_code = 400, detail=f'{str(e)} {traceback.format_exc()}')

@app.get("/dummy")
def get_dummy():
  return {
    "message" : "Got an API"
  }

@app.get("/categories/{city}")
async def categories(city):
  try:
    category_table = await get_categories(city=city)
    return category_table
  except Exception as e: 
    return HTTPException(status_code=400, detail=str(e))