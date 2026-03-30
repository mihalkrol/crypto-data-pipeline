import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

today_clean_db = BASE_DIR / "data" / "crypto_data_today_clean.db"
cleaned_db = BASE_DIR / "data" / "crypto_data_cleaned.db"


def run_load():
    # Read data from today's cleaned database
    today_conn = sqlite3.connect(today_clean_db)
    today_df = pd.read_sql("SELECT * FROM crypto_prices_today_clean", today_conn)
    today_conn.close()

    # Get today's date from the data
    today_date = today_df['date'].iloc[0]

    # Connect to cleaned database
    cleaned_conn = sqlite3.connect(cleaned_db)

    # Check if today's date already exists
    cursor = cleaned_conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM crypto_prices_cleaned WHERE date = ?", (today_date,))
    count = cursor.fetchone()[0]

    if count > 0:
        print("Cleaned Database up to date")
    else:
        # Append today's data
        today_df.to_sql("crypto_prices_cleaned", cleaned_conn, if_exists="append", index=False)
        cleaned_conn.commit()
        print(f"Appended {len(today_df)} records for {today_date}")

    cleaned_conn.close()


if __name__ == "__main__":
    run_load()
