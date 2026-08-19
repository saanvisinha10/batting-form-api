from typing import Dict, Any, Optional, List

MOCK_BATTER_HISTORY: Dict[str, List[Dict[str, Any]]] = {
    "virat_kohli": [
        {
            "match_id": "match_101",
            "innings_id": "innings_101_1",
            "runs": 15,
            "balls": 4,
            "fours": 2,
            "sixes": 1,
            "is_out": False
        },
        {
            "match_id": "match_100",
            "innings_id": "innings_100_1",
            "runs": 82,
            "balls": 53,
            "fours": 6,
            "sixes": 4,
            "is_out": False
        },
        {
            "match_id": "match_99",
            "innings_id": "innings_99_1",
            "runs": 51,
            "balls": 43,
            "fours": 3,
            "sixes": 2,
            "is_out": True
        }
    ]
}

def calculate_batting_form(batter_id: str) -> Optional[Dict[str, Any]]:
    formatted_id = batter_id.lower().replace(" ", "_")
    history = MOCK_BATTER_HISTORY.get(formatted_id)
    
    if not history:
        return None

    total_runs = sum(perf["runs"] for perf in history)
    total_balls = sum(perf["balls"] for perf in history)
    total_fours = sum(perf["fours"] for perf in history)
    total_sixes = sum(perf["sixes"] for perf in history)
    matches_played = len(history)

    overall_sr = round((total_runs / total_balls) * 100, 2) if total_balls > 0 else 0.0

    performances = []
    for perf in history:
        sr = round((perf["runs"] / perf["balls"]) * 100, 2) if perf["balls"] > 0 else 0.0
        performances.append({
            "match_id": perf["match_id"],
            "innings_id": perf["innings_id"],
            "runs": perf["runs"],
            "balls": perf["balls"],
            "fours": perf["fours"],
            "sixes": perf["sixes"],
            "strike_rate": sr,
            "is_out": perf["is_out"]
        })

    display_name = batter_id.replace("_", " ").title()

    return {
        "batter_name": display_name,
        "matches_played": matches_played,
        "total_runs": total_runs,
        "total_balls": total_balls,
        "overall_strike_rate": overall_sr,
        "total_fours": total_fours,
        "total_sixes": total_sixes,
        "recent_performances": performances
    }
