# Crypto Data Pipeline

## Overview

This project is a simple batch data pipeline that fetches cryptocurrency market data from the CoinGecko API, stores daily CSV snapshots, and appends the data to a SQLite database for historical tracking and analysis.

The project was built as part of my data engineering learning path, with a focus on Python, SQL, data storage, and basic visualization.
My main goal was to understand how pipelines work and how work of data engineer can look like.

## Features

- Fetches cryptocurrency market data from the CoinGecko API
- Selects and cleans relevant columns
- Stores a daily CSV snapshot
- Appends new records to a SQLite database
- Builds a growing historical dataset over time
- Supports SQL-based analysis in a notebook
- Includes matplotlib visualizations for selected coins

## Tech stack

- Python
- pandas
- requests
- SQL
- matplotlib
- 
## How it works
1. The pipeline sends a request to the CoinGecko API
2. The response is loaded into a pandas DataFrame
3. Relevant columns are selected and renamed
4. Coin symbols are normalized to uppercase
5. The current date is added as a snapshot date
6. A daily CSV file is saved
7. The same data is appended to a SQLite table for historical storage
8. The data is then used for analysis and visualization in a separate notebook

## Analysis and visualization

The notebook:

- queries the SQLite database using SQL
- analyzes historical price data
- selects a subset of cryptocurrencies
- visualizes price trends over time using matplotlib

This demonstrates how the collected data can be used for downstream analysis and supports an end-to-end workflow from data ingestion to insights.


## Project structure

```text
crypto-data-pipeline/
│
├── data/
│   ├── crypto_YYYY-MM-DD.csv # .csv with date snapshots
│   └── crypto_data_all.db # whole database
│
├── notebooks/
│   └── sql_queries.ipynb
│
├── src/
│   └── extract.py
│
├── requirements.txt
└── README.md


