# Project 2: Cloud Data Warehouse

## Project Introduction

A music streaming startup, Sparkify, has grown their user base and song database and want to move their processes and data onto the cloud. Their data resides in S3, in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

As the data engineer, we are tasked with building an ETL pipeline that extracts data from S3, stages them in Redshift, and transforms data into a set of dimensional tables for their analytics team to continue finding insights into what songs their users are listening to.


![](https://github.com/phphoebe/Udacity-Data-Engineering-with-AWS/blob/main/Course%202-Cloud%20Data%20Warehouses/Project%202-Data%20Warehouse/images/sparkify-s3-to-redshift-etl.png)

### Tools used
* Python, SQL
* Juypter Notebook
* AWS Services (Redshift, S3, EC2, IAM, VPC)


## Project Summary
### Data Exploration

* Using the AWS CLI to list bucket objects

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

### ETL Pipeline


### Database Schema

* **Staging Tables**

* **Fact Table**

* **Dimension Tables**
