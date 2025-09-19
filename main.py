from fastapi import FastAPI
from typing import Dict

app = FastAPI()

# Mock data
mock_profile_data = [
    [100, 200, 300, 400],
    [50, 80, 120, 160],
    [50, 120, 180, 240],
    [50, 120, 180, 240],
  ]

# Simple GET route
@app.get("/profile")
async def get_profile():
    return mock_profile_data
