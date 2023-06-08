# Project 2: Cloud Data Warehouse

## Project Introduction

A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

As the data engineer, we are tasked with building an ETL pipeline that extracts data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights into what songs their users are listening to.


![](https://github.com/phphoebe/Udacity-Data-Engineering-with-AWS/blob/main/Course%202-Cloud%20Data%20Warehouses/Project%202-Data%20Warehouse/images/sparkify-s3-to-redshift-etl.png)

### Tools used
* Python, SQL
* Juypter Notebook
* AWS Services (Redshift, S3, EC2, IAM, VPC, Boto3, CLI)

## AWS Configuration
Creating resources on AWS using the AWS management console to support the Redshift data warehouse. 
#### 1. Create an IAM Role
* create a `myRedshiftRole` IAM role with the `AmazonS3ReadOnlyAccess` permission policy attached
#### 2. Create Security Group for Redshift
* create a `redshift_security_group` security group that authorizes Redshift cluster access (with the default VPC)
#### 3. Create an IAM User for Redshift
* create an IAM user with below two permission policies attached, and create and save the `Access key` and `Security access key`
    * `AmazonRedshiftFullAccess`
    * `AmazonS3ReadOnlyAccess`
#### 4. Launch a Redshift Cluster
* create the `redshift-cluster-1` cluster that attaches the `myRedshiftRole` role and the `redshift_security_group` security group 

> ***NOTE:** Make sure to delete the cluster each time finish working to avoid large, unexpected costs*

## Project Data Exploration

* Using the [AWS CLI S3 commands](https://docs.aws.amazon.com/cli/latest/userguide/cli-services-s3-commands.html) to list bucket objects

```
aws configure
AWS Access Key ID: {KEY}
AWS Secret Access Key: {SECRET}

aws s3 ls s3://udacity-dend/log_data/2018/11/
aws s3 ls s3://udacity-dend/song_data/A/A/A/
```

![](https://github.com/phphoebe/Udacity-Data-Engineering-with-AWS/blob/main/Course%202-Cloud%20Data%20Warehouses/Project%202-Data%20Warehouse/images/log_data.png)
![](https://github.com/phphoebe/Udacity-Data-Engineering-with-AWS/blob/main/Course%202-Cloud%20Data%20Warehouses/Project%202-Data%20Warehouse/images/song_data.png)

* Download [sample_date](https://github.com/phphoebe/Udacity-Data-Engineering-with-AWS/tree/main/Course%202-Cloud%20Data%20Warehouses/Project%202-Data%20Warehouse/sample_data) to local to explore the data (check data type etc.)

```
aws s3 cp s3://udacity-dend/song_data/A/A/A/TRAAAAK128F9318786.json sample_data/TRAAAAK128F9318786.json

aws s3 cp s3://udacity-dend/log_data/2018/11/2018-11-30-events.json sample_data/2018-11-30-events.json

aws s3 cp s3://udacity-dend/log_json_path.json sample_data/log_json_path.json
```

## ETL Pipeline

* [etl_test.ipynb](https://github.com/phphoebe/Udacity-Data-Engineering-with-AWS/blob/main/Course%202-Cloud%20Data%20Warehouses/Project%202-Data%20Warehouse/etl_test.ipynb) - test AWS Configurations and the ETL process, including validation and example analytical queries
* [sql_queries.py](https://github.com/phphoebe/Udacity-Data-Engineering-with-AWS/blob/main/Course%202-Cloud%20Data%20Warehouses/Project%202-Data%20Warehouse/sql_queries.py) - a collection of SQL queries for `create_tables.py` and `etl.py`

1. Run [create_tables.py](https://github.com/phphoebe/Udacity-Data-Engineering-with-AWS/blob/main/Course%202-Cloud%20Data%20Warehouses/Project%202-Data%20Warehouse/create_tables.py) to create Staging, Fact and Dimension table schema using command `python3 create_tables.py`
* `drop_tables` - drop table if exists 
* `create_tables` - create tables

2. Run [etl.py](https://github.com/phphoebe/Udacity-Data-Engineering-with-AWS/blob/main/Course%202-Cloud%20Data%20Warehouses/Project%202-Data%20Warehouse/etl.py) to complete the ETL process using command `python3 etl.py`
* `load_staging_tables` 
    - load/copy raw data from S3 buckets to Redshift staging tables
    - reference: [Using the COPY command to load from Amazon S3](https://docs.aws.amazon.com/redshift/latest/dg/t_loading-tables-from-s3.html)
* `insert_tables` 
    - transforming staging tables to star-schema fact & dimension tables for song play analysis

## Database Schema for Song Play Analysis

* ### Staging Tables 

```
staging_events 
          - artist          
          - auth
          - firstName
          - gender
          - itemInSession
          - lastName
          - length
          - level
          - location
          - method
          - page
          - registration
          - sessionId
          - song
          - status
          - ts
          - userAgent
          - userId

staging_songs 
          - artist_id        
          - artist_latitude
          - artist_location
          - artist_longitude
          - artist_name
          - duration
          - num_songs
          - song_id
          - title
          - year
```
* ### Fact Table 


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
* ### Dimension Tables 

```
users 
          - user_id           PRIMARY KEY
          - first_name
          - last_name
          - gender
          - level

songs 
          - song_id           PRIMARY KEY
          - title
          - artist_id
          - year
          - duration

artists 
          - artist_id         PRIMARY KEY
          - name
          - location
          - latitude
          - longitude

time 
          - start_time        PRIMARY KEY
          - hour
          - day
          - week
          - month
          - year
          - weekday
```
> **NOTE:** 
> * _The `SERIAL` command in Postgres is not supported in Redshift. The equivalent in redshift is `IDENTITY(0,1)`, which you can read more on in the [Redshift Create Table Docs](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_TABLE_NEW.html)._
> * _Amazon Redshift automatically assigns a `NOT NULL` condition to columns defined as `PRIMARY KEY`. You don't need to specify it separately. This can simplify the table create scripts._

## Setup & Run Jupyter Notebooks in VS Code w/ Virtual Env & Kernels

* create a virtual environment
  ```
  python3 -m venv udacity-dend 
  ```
* activate the virtual env
  ```
  source udacity-dend/bin/activate
  ```
* Installation 

  ```
  pip install jupyterlab
  
  pip install ipykernel
  ```
  _Validate that the install has succeeded by running `jupyter-lab` from your command line. A new tab should open in your browser, with the JupyterLab application running._
  
  * install useful Python packages in this virtual env
  

  ```
  pip install boto3
  pip install psycopg2
  ```
  
* register the new virtual env with Jupyter so that you can use it within JupyterLab

    ```
    python3 -m ipykernel install --user --name=‘udacity-dend‘ 
    ```
