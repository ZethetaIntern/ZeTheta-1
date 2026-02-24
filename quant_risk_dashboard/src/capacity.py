def estimate_capacity(avg_daily_volume: float,
                      turnover: float,
                      participation_rate: float = 0.05) -> float:
    
    if turnover == 0:
        return 0.0
    
    return (avg_daily_volume * participation_rate) / turnover