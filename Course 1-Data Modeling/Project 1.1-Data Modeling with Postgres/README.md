# Project 1.1 - Data Modeling with Postgres

## Project Introduction

#### Description
* Model user activity data (JSON) to create a database and ETL pipeline in Postgres for a music streaming app startup called Sparkify
* Define Fact and Dimension tables for a STAR schema optimized for queries on song play analysis
* Insert data into new tables

Sparkify's Analytics team will be able to query the newly designed relational database with ease to understand user behaviors such as what songs users are listening to.

#### Tools used
* PostgreSQL
* Python
* Jupyter Notebook


## Project Summary

### Project Files 

```
|____data
| |____log_data                         # simulated app user activity logs
| |____song_data                        # metadata about a song and the artist of that song
|
|____notebook
| |____etl.ipynb                        # ETL processes to develop ETL builder 
| |____test.ipynb                       # to test ETL builder
|
|____script
| |____create_tables.py                 # script to create the Sparkify databases and the Fact & Dimension tables
| |____etl.py                           # ETL pipeline builder
| |____sql_queries.py                   # ETL pipeline builder help - DDL queries & Find Song DQL query
```



### Database Schema 

* #### Fact Table 


```
songplays 
          - songplay_id       PRIMARY KEY
          - start_time
          - user_id
          - level
          - song_id
          - artist_id
          - session_id
          - duration
          - user_agent
```

* #### Dimension Tables


```
users 
          - user_id           PRIMARY KEY
          - first_name
          - last_name
          - gender
          - level
```
```
songs 
          - song_id           PRIMARY KEY
          - title
          - artist_id
          - year
          - duration
```
```
artists 
          - artist_id         PRIMARY KEY
          - name
          - location
          - latitude
          - longitude
```
```
time 
          - start_time        PRIMARY KEY
          - hour
          - day
          - week
          - month
          - year
          - weekday
```
* #### Entity Relationship Diagram (ERD)

![](https://github.com/phphoebe/Udacity-Data-Engineering-with-AWS/blob/main/Course%201-Data%20Modeling/Project%201.1-Data%20Modeling%20with%20Postgres/Sparkify%20ERD.png)



### Steps to run the Python scripts
1. Run `create_tables.py` in the terminal to create/reset databases/tables using command ```python create_tables.py```
2. Run `etl.py` in the terminal to complete the ***ETL process*** using command ```python etl.py```

#### ETL Processes/ETL Builder Explain
* process the `song_data` dataset to create the `songs` and `artists` dimensional tables, and insert record into the tables
* process the `log_data` dataset to to create the `time` and `users` dimensional tables, as well as the `songplays` fact table; and insert records into the tables
* run `test.ipynb` to confirm the creation of the tables with the correct columns, and to confirm that the records were successfully inserted into each table


> ***NOTE:** You will not be able to run `test.ipynb`, `etl.ipynb`, or `etl.py` until you have run `create_tables.py` at least once to create the sparkifydb database, which these other files connect to.*
