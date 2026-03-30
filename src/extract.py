import requests
import pandas as pd
import sqlite3
from datetime import datetime
from pathlib import Path

# API config
url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 50,
    "page": 1,
    "price_change_percentage": "24h,7d,30d"
}


def run_extract():
    response = requests.get(url, params=params, timeout=30)
    response.raise_for_status()
    data = response.json()

    df = pd.DataFrame(data)

    df = df[
        [
            "name",
            "symbol",
            "current_price",
            "market_cap",
            "market_cap_rank",
            "total_volume",
            "price_change_percentage_24h",
            "price_change_percentage_7d_in_currency",
            "price_change_percentage_30d_in_currency",
        ]
    ]

    df = df.rename(
        columns={
            "price_change_percentage_24h": "price_change_24h",
            "price_change_percentage_7d_in_currency": "price_change_7d",
            "price_change_percentage_30d_in_currency": "price_change_30d",
        }
    )

    df["symbol"] = df["symbol"].str.upper() # Convert symbols to uppercase for consistency

    today = datetime.now().date()
    df["date"] = today
#PATHS
    project_root = Path(__file__).resolve().parent.parent
    data_dir = project_root / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    csv_path = data_dir / f"crypto_{today}.csv" 
    db_path = data_dir / "crypto_data_raw.db" 

    df.to_csv(csv_path, index=False)

    conn = sqlite3.connect(db_path)
    try:
        df.to_sql("crypto_prices", conn, if_exists="append", index=False)
    finally:
        conn.close()

    
    print(f"Saved {len(df)} rows to {csv_path} and {db_path}")

if __name__ == "__main__":
    run_extract()