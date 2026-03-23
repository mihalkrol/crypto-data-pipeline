import requests
import pandas as pd
from datetime import datetime

#API import
url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 50,
    "page": 1,
    "price_change_percentage": "24h,7d,30d"
}

response = requests.get(url, params=params, timeout=30)
response.raise_for_status()
data = response.json()

df = pd.DataFrame(data)
#API column names of interest
df = df[[
    "name",
    "symbol",
    "current_price",
    "market_cap",
    "market_cap_rank",
    "total_volume",
    "price_change_percentage_24h",
    "price_change_percentage_7d_in_currency",
    "price_change_percentage_30d_in_currency"
]]
#rename few columns for better readability

df = df.rename(columns={
    "price_change_percentage_24h": "price_change_24h",
    "price_change_percentage_7d_in_currency": "price_change_7d",
    "price_change_percentage_30d_in_currency": "price_change_30d"
})

# convert symbol to uppercase
df["symbol"] = df["symbol"].str.upper()

print(df.head())

#today's date
today = datetime.now().date()
df["date"] = today

filename = f"../data/crypto_{today}.csv"

# save to csv, with date
df.to_csv(filename, index=False)

# saving to sqlite database
import sqlite3

conn = sqlite3.connect("../data/crypto_data_all.db")

df.to_sql("crypto_prices", conn, if_exists="append", index=False)

conn.close()