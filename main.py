from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.configure.connection.mongodb import client
from src.app.naturefit import router as nf_router

# Define the FastAPI app
app = FastAPI()



@app.get("/")
async def root():
    return {"message": "Welcome to the chatbot API!"}

@app.on_event("startup")
async def startup_db():
    # Ensure the connection to MongoDB is working
    try:
        print("Connecting to MongoDB...")
        await client.server_info()  # This checks the connection
        print("MongoDB connection successful!")
    except Exception as e:
        print("Could not connect to MongoDB:", e)

app.include_router(nf_router.router)