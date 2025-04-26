from fastapi import FastAPI
import requests

app = FastAPI()

@app.get("/api/data")
async def get_data():
    processed_data = {
        'result': 'dsadsadsa'
    }
    
    return processed_data