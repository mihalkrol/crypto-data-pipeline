# Crypto Data Pipeline

## Overview

This project is a batch data pipeline that fetches cryptocurrency market data from the CoinGecko API and processes it using an orchestrated ELT workflow.

The project evolved from a simple data extraction script into a more production-style data pipeline using Apache Airflow. It now includes multiple stages of data processing, data quality handling, and clear separation between raw and cleaned data layers.

The main goal of this project is to demonstrate practical data engineering concepts such as orchestration, data modeling, idempotency, and pipeline structuring.

---

## Features

- Fetches cryptocurrency market data from the CoinGecko API
- Orchestrates workflow using Apache Airflow
- Implements extract → clean → load (ELT) pipeline
- Stores raw data separately from processed data
- Performs data cleaning and deduplication using pandas
- Prevents duplicate daily records (idempotent pipeline behavior)
- Stores processed data in a SQLite database
- Enables downstream SQL analysis and visualization

---

## Tech stack

- Python
- Apache Airflow
- pandas
- requests
- SQL (SQLite)
- matplotlib

---

## Pipeline architecture

The pipeline follows a layered data approach:

API → RAW → CLEAN → DATABASE

- Extract – pulls data from CoinGecko API and stores raw data  
- Clean – removes duplicates and standardizes data using pandas  
- Load – inserts clean, deduplicated data into the final database  

---

## How it works

1. Airflow triggers the pipeline on a schedule
2. Data is fetched from the CoinGecko API (extract stage)
3. Raw data is stored for traceability
4. Data is cleaned and deduplicated using pandas
5. Clean data is inserted into a structured SQLite database
6. The pipeline ensures no duplicate records are added for the same day

---

## Analysis and visualization

The notebook:

- queries the SQLite database using SQL
- analyzes historical cryptocurrency data
- selects a subset of coins
- visualizes price trends using matplotlib

This demonstrates how the pipeline supports downstream analytics and completes an end-to-end data workflow.

---

## Project structure

crypto-data-pipeline/
│
├── dags/                  # Airflow DAG definitions
│
├── data/
│   ├── raw/               # raw data layer
│   └── processed/         # cleaned data layer
│
├── notebooks/
│   └── sql_queries.ipynb
│
├── src/
│   ├── extract.py
│   ├── clean.py
│   └── load.py
│
├── config/                # configuration files (if applicable)
│
├── requirements.txt
└── README.md

---

## Versioning

### V1
- Simple data extraction script
- Stored CSV snapshots and appended to SQLite
- No orchestration or data layering

### V2 (current)
- Introduced Airflow orchestration
- Implemented full ELT pipeline (extract → clean → load)
- Added raw and cleaned data layers
- Improved data quality with deterministic deduplication (pandas)
- Enhanced structure and maintainability

---

## Future improvements

- Replace SQLite with PostgreSQL or DuckDB
- Add data validation tests (e.g. Great Expectations)
- Introduce dbt for transformations
- Add dashboard (Streamlit / Superset)
- Implement partitioning strategy for data storage
