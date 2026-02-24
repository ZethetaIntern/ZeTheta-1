import pandas as pd

def load_strategy_returns(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["date"])
    df.set_index("date", inplace=True)
    return df

def load_market_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["date"])
    df.set_index("date", inplace=True)
    return df