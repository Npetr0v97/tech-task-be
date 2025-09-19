from fastapi import FastAPI,HTTPException
import data
app = FastAPI()



@app.get("/profile")
async def get_profile():
    return data.mock_profile_data

@app.get("/config")
async def get_config(type: str ):
    if type == "profile":
        return data.mock_profile_config
    elif type == "transactions":
        return data.mock_transactions_config
    else:
        raise HTTPException(status_code=404, detail=f"Config type '{type}' not found")

@app.get("/transactions")
async def get_transcations():
    return data.mock_transactions

