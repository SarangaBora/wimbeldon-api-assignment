# main.py

from fastapi import FastAPI, HTTPException, Query
from data import wimbledon_data

app = FastAPI()

@app.get("/wimbledon")
def get_wimbledon_result(year: int = Query(..., ge=1877)):
    if year not in wimbledon_data:
        raise HTTPException(status_code=404, detail="Data for the given year not found.")
    
    data = wimbledon_data[year]
    return {
        "year": year,
        **data
    }
