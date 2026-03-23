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

## Data collected

The pipeline collects the following fields:

- name
- symbol
- current_price
- market_cap
- market_cap_rank
- total_volume
- price_change_24h
- price_change_7d
- price_change_30d
- date

## Tech stack

- Python
- pandas
- requests
- SQL
- matplotlib

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
