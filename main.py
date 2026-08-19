from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from schemas import BattingFormResponse
from services import calculate_batting_form

app = FastAPI(
    title="Batting Form API",
    description="Microservice for tracking a batter's form across recent innings.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Health Check"])
def root():
    return {"message": "Batting Form API is live"}

@app.get("/health", tags=["Health Check"])
def health():
    return {"status": "ok"}

@app.get("/batting-form/{batter_id}", response_model=BattingFormResponse, tags=["Batting Form"])
def get_batting_form(batter_id: str):
    result = calculate_batting_form(batter_id)
    if not result:
        raise HTTPException(status_code=404, detail=f"Batter form data for '{batter_id}' not found.")
    return result
