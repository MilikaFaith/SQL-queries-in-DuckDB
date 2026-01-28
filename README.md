# SQL NYC TAXI TRIP OPERATIONS ANALYSIS
This project was completed as part of a SQL masterclass, where a base repository was provided and each participant worked independently to demonstrate SQL proficiency by analyzing NYC taxi operations.

## 📌Business Context & Key Questions
The analysis seeks to evaluate the company's operational and financial performance over the past decade within an evolving mobility landscape.It focuses on understaning trip behavior, revenue trends,vendor performance,customer payment prefrences and geographic patterns across time.
### Operational Performance
+ What does an average taxi trip look like in terms of distance, fare, speed, and cost efficiency?
+ How does taxi demand fluctuate throughout the day based on hourly trip volumes?
### Financial Performance
+ How have revenue, fares, tips, and surcharges trended over time, and are there observable seasonal patterns?
+ Which payment methods generate the highest number of trips and revenue?
+ How does revenue performance vary by borough, including average revenue per mile and tipping behavior?
+ How does annual revenue change year over year, and how does each year compare to the previous one?

## 📑Dataset Overview
The analysis uses NYC taxi trip data spanning a decade [2015 - 2025], capturing operational and financial details to evaluate company performance.
### This includes;
+ **Tables:** yellow_taxi_trip_data,green_taxi_trip_data,taxi_zone_lookup.
+ **Trips:** pickup and dropoff timestamps,trip distance,calculated durations and speed metrics.
+ **Financials:** fares,total amount,tips,surcharges,total revenue and payment types.
+ **Vendors:** Vendorid's.
+ **Geography:** pickup and dropoff locations, boroughs,zones.

Each raw represents a single trip,enabling analysis at trip,hourly,monthly and early levels.The dataset provides the foundation for answering key business questions on operational effeciency,revenue trends,customer behavior and geographic performance
## 🔨Approach & Workflow
### 1. Understanding the Business Goals and Requirements.
+ Understanding Company performance over the face of a decade in terms of;
  +  **Operations:** Trips,Vendors,Customer behavior.
  +  **Revenue:** Location,time.
### 2. Importing and Contextualizing the Data.
+ Cloned the resipository to my git for data retrival.
+ Loaded the data into my DuckDB environment from the official TLC NYC trip record data using the forked python data pipline into readble SQL tables.
+ Loaded the taxi_zone_lookup_table (link) to facilitate the analysis of boroughs and zones performance.
+ Verified the dataset against the business context, ensuring completeness and relevance in the required form and timeframe to support the intended analysis.
### 3. Data Preparation - Cleaned, Validated & Standardized.
+ Checked for  missing values in critical feilds: fares, trips,passenger counts,vendorids,ratecodeids,surcharges.
+ Checked for Negative/zero/invalid records: zero or negative fares,trip_distance,surcharges.
+ Checked for invalid timestamps: dropoff_datetime < pickup_datetime
+ Checked for unrealistic durations: dropoff time - pickup time > 8 hour interval.
+ Checked for Duplicates: vendorid,trips is > 1
+ Checked for irrelevant data: Data not within the 10 year decade [ 2015 - 2025]
+ Created a complete Data Quality Check Table (Link to Code).
### 4. KPI Design and Analytical SQL Queries
+ **Operational Analytics performance**
  + Operational trip summary performance for both the green and yellow taxi trip data.
     + Utilized multiple **CTE's to break the steps into 3 modularized steps**.
      1. **Base CTE:** Selects core taxi trip details,calculates trip duration in minutes,enriches each trip with location context through JOINS and filters out any invalid or inconsistent records ensuring data quality.
      2. **Metrics CTE:** Builds on the base to give the average speed per trip and fare per mile while handling any edge cases such as zero durations or zero distance trips ensuring the analytical values remain reliable.
      3. **Main Query:** It aggregates the taxi trip data, giving a summary of the total trips,average distance,average fare, average trip duration by vendor,year,month and pickup and drop_of borough.Giving a trend and performance analysis summary over time and across locations wrapped into a trip_summaries_table.
         
      *NB//The green_taxi_trip summaries query table contains a deduplicate CTE that utilizes Window Functions (ROW_NUMBER()) that removes duplicate trip records by    identifying multiple entries for the same pickup and drop_off timestamps,retaining the most representative version of each trip based on the highest total amount.*
  +  Hourly operational perfomance trend.
     + Utilized **UNION ALL** to merge the yellow and green taxi datasets into a unified view of pickup activity,using **CASE** statementes to categorize the pickup times into hourly AM/PM buckets,time extraction,type conversion and padding to summarize the trip volumes by year and hour, allowing for demand pattern comparison across taxi services and hourly operational performance trend.
 
+ **Financial Analytics Performance**
  +  **Financial performance trend over time.**
     + Built a query that summarizes monthly revenue by aggregating key components of total revenue including fares,tips and surcharges.Calculating both absolute values and the percentage contribution of each component to the overall monthly revenue, providing insight into the composition of earnings over time.Invalid or missing monetray values are filtered as well using **COALLESE and WHERE clauses** to ensure data quality, groups trips by year and months,and the results are formated for easy trend analysis and reporting.
  +  **Customer Payment distribution.**
     + Utilized a **CASE statement** to categorize the numeric payment codes into descriptive payment method labels "'Credit Card', 'Cash', and 'No Charge'", aggregated trip counts and total revenue by payment method,month and year,formatting the results to reveal customer payment prefrences and identifying the most revenue generating methods over time,still ensuring invalid or zero value trips are filtered out.
  +  **Zonal Profitability performnace.**
     + Linked the taxi trip table with the taxi_zone_lookup table using a **LEFT JOIN** and aggregated total revenue,fares and tips by borough,month and year and calculated average revenue per mile and averge tip revealing which zones contribute most profits over time with the results ordered by year,month and revenue.
  +  **Year over year & Month over Month Revenue Growth.**
     + Utilized multiple **CTE's with Window Functioncs(LAG())** to build a pipeline that calculates monthly and annual revenue growth,both month-over-month and year-over-year growth percentages giving insight on short and long term revenue trends.
  +  **Borough revenue flow.**
     + Built a query that identifies high and low value service areas by calculating the total and average revenue per trip,per mile and per minute across pickup and drop-off boroughs,enabling insight into borough flow  revenue perormance
  +   **Vendor performance Analysis.**
      + To asses vendor performance in terms of total revenue contribution and tips ,built a query that aggregates the trips by vendor,year and month summarizing the total average revenue and tips per trip ,revealing the vendors that contribute most to the overall revenue and tip income.
### 5. Integrating Data into Power BI for Visualization & Reporting.

--- 
## Original project readme
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
