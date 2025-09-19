from fastapi import FastAPI
from typing import Dict

app = FastAPI()

# Mock data
mock_profile_data: Dict[str, dict] = {
    "1": {"name": "Alice", "age": 25},
    "2": {"name": "Bob", "age": 30},
}

# Simple GET route
@app.get("/profile/{user_id}")
async def get_profile(user_id: str):
    data = mock_profile_data.get(user_id)
    if not data:
        return {"error": f"No profile data found for user {user_id}"}
    return data
