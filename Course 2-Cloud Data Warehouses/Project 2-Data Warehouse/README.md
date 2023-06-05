# Project 2: Cloud Data Warehouse

## Project Introduction



![](https://github.com/phphoebe/Udacity-Data-Engineering-with-AWS/blob/main/Course%202-Cloud%20Data%20Warehouses/Project%202-Data%20Warehouse/images/sparkify-s3-to-redshift-etl.png)

**Description**


**Tools used**


## Data Exploration

Using the AWS CLI to list bucket objects

```
aws configure
AWS Access Key ID: {KEY}
AWS Secret Access Key: {SECRET}

aws s3 ls s3://udacity-dend/log_data/2018/11/
aws s3 ls s3://udacity-dend/song_data/A/A/A/
```

![](https://github.com/phphoebe/Udacity-Data-Engineering-with-AWS/blob/main/Course%202-Cloud%20Data%20Warehouses/Project%202-Data%20Warehouse/images/log_data.png)
![](https://github.com/phphoebe/Udacity-Data-Engineering-with-AWS/blob/main/Course%202-Cloud%20Data%20Warehouses/Project%202-Data%20Warehouse/images/song_data.png)

Download [sample_date](https://github.com/phphoebe/Udacity-Data-Engineering-with-AWS/tree/main/Course%202-Cloud%20Data%20Warehouses/Project%202-Data%20Warehouse/sample_data) to local to explore the data (check data type etc.)

```
aws s3 cp s3://udacity-dend/song_data/A/A/A/TRAAAAK128F9318786.json sample_data/TRAAAAK128F9318786.json

aws s3 cp s3://udacity-dend/log_data/2018/11/2018-11-30-events.json sample_data/2018-11-30-events.json

aws s3 cp s3://udacity-dend/log_json_path.json sample_data/log_json_path.json
```

## ETL Pipeline


## Database Schema
