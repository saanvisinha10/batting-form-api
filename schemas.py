from pydantic import BaseModel
from typing import List

class InningsPerformance(BaseModel):
    match_id: str
    innings_id: str
    runs: int
    balls: int
    fours: int
    sixes: int
    strike_rate: float
    is_out: bool

class BattingFormResponse(BaseModel):
    batter_name: str
    matches_played: int
    total_runs: int
    total_balls: int
    overall_strike_rate: float
    total_fours: int
    total_sixes: int
    recent_performances: List[InningsPerformance]
