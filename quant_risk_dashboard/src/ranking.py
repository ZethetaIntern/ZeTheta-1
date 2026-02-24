import pandas as pd
from .performance import sharpe_ratio
from .risk import max_drawdown

def strategy_ranking(returns_df: pd.DataFrame) -> pd.DataFrame:
    
    results = []
    
    for col in returns_df.columns:
        r = returns_df[col]
        sharpe = sharpe_ratio(r)
        mdd = max_drawdown(r)
        
        score = sharpe + mdd  
        
        results.append({
            "Strategy": col,
            "Sharpe": sharpe,
            "Max_Drawdown": mdd,
            "Score": score
        })
    
    df = pd.DataFrame(results)
    return df.sort_values("Score", ascending=False)