import sqlite3
import pandas as pd
from pathlib import Path


def run_clean():
    BASE_DIR = Path(__file__).resolve().parent.parent

    conn = sqlite3.connect(BASE_DIR / "data" / "crypto_data_raw.db")

    # Read all data from the table
    df = pd.read_sql("SELECT * FROM crypto_prices", conn)
    
    # Filter to the latest date
    df = df[df['date'] == df['date'].max()]
    
    # Deduplicating by crypto symbol using pandas
    df = df.drop_duplicates(subset=['symbol'], keep='first')

    # Save cleaned dataframe to SQLite database
    output_db_path = BASE_DIR / "data" / "crypto_data_today_clean.db"
    output_conn = sqlite3.connect(output_db_path)
    df.to_sql("crypto_prices_today_clean", output_conn, if_exists="replace", index=False)
    output_conn.close()
    print(f"Data saved to {output_db_path}")


if __name__ == "__main__":
    run_clean()

