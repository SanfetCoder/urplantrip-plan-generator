from fastapi import FastAPI

# Create an app for this API
app = FastAPI()

# At root route
@app.get("/")
async def root():
  return {"message": "Hello World"}
