# SQL-queries-in-DuckDB
Hands-on SQL practice using DuckDB to explore and analyze the NYC Taxi dataset.
This repository contains materials for the SQL AMA Workshop, starting with DuckDB as our in-process analytical SQL engine and the NYC Taxi Dataset as our primary practice dataset.
Learn more about DuckDB from the docs: https://duckdb.org/docs/stable/
Explore the dataset host site: [NYC TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
## 📌 Objectives
+ Build a solid foundation in SQL syntax and relational query concepts.
+ Understand how DuckDB operates as a lightweight but high-performance analytics engine.
+ Gain practical experience querying a real-world dataset without provisioning or managing a persistent database server.
+ Learn to integrate DuckDB into an analytics workflow for fast iteration and reproducible results.
## 🧰 Our Stack
To ensure a smooth learning experience, we’ll use a local-first, minimal-dependency analytics stack that participants can set up in minutes:
+ **DuckDB** – In-process analytical database, our primary SQL execution engine.
+ **Python 3.10+** – Host environment for running DuckDB queries programmatically.
+ **Jupyter Notebooks** – Interactive development and explanation of query logic.
+ **NYC Taxi Dataset** – Primary data source with millions of trip records.
+ **Parquet & CSV** – File formats we’ll query directly without importing into a DB.
## 🛠 Why DuckDB?
DuckDB is an in-process OLAP (Online Analytical Processing) database designed for fast, interactive analytics directly within your working environment.
a columnar, vectorized execution engine optimized for large-scale aggregations and joins.
Read more from the official documentation: https://duckdb.org/why_duckdb
