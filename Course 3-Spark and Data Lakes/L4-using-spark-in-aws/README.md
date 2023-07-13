## Using Spark in AWS with Data Lakes

### Lesson Outline

* Data Lakes in AWS
    * _Structured and Unstructured Data_
    * _AWS S3 Data Lakes_
* Using Spark on AWS
    * _EC2 instances_
    * _AWS EMR_
    * _AWS Glue_
* AWS Glue
    * _Glue Service Components_
    * _Spark Glue jobs_
    * _Creating and Running Glue jobs_

### Lesson Objectives 

<img src="../L4-using-spark-in-aws/images/0-lesson_objectives.png" width=70% height=70%>

___

### Data Lakes in AWS

A lake is a large body of water. It is usually a naturally occurring feature. If your organization has large amounts of data somewhere, you have a data lake! 
* in an `unstructured` format (Text, Multimedia, etc.)
* or `semi-structured` format (CSV, JSON, Parquet, and other formats)

Data Lakes are not a specific technology. They can be implemented using many types of file storage systems. 

* In AWS, the most common way to store files is in S3. We can implement data lakes using S3 storage. 
* S3 buckets are an abstraction of storage similar to HDFS. They make it possible to store an almost unlimited amount of data and files.
* In the AWS Cloud, S3 buckets make file storage availabe on a network and enable systems and people to exchange data. 

    <img src="../L4-using-spark-in-aws/images/1-data_lakes_in_aws.png" width=40% height=70%>

In the rest of the lesson, we'll see how to use S3 data lake to store and process data with Spark


___ 

### Using Spark on AWS

Choices to rent a cluster of machines on AWS to run Spark: 

* EMR (Elastic MapReduce)
    * AWS managed Spark service
    * a scalable set of EC2 machines already configured to run Spark
    * no need to manage the systems, only configure the necessary cluster resources
    * Distributed Computing
    * HDFS Installed
    * Billing Model: EC2 costs
    * Provisioning: Automated

* EC2
    * Use AWS Elastic Compute (EC2) machines 
    * Install and configure Spark and HDFS yourself
    * Distributed Computing
    * HDFS Installed
    * Billing Model: EC2 costs
    * Provisioning: Self Installed

* Glue
    * A serverless Spark environment with added libraries like the Glue Context and Glue Dynamic Frames
    * Also interfaces with other AWS data services like Data Catalog and AWS Athena
    * Distributed Computing
    * Serverless: Yes
    * HDFS Installed
    * Billing Model: Job Duration
    * Provisioning: Zero Provisioning


We'll focus on using the AWS Glue tool to run Spark scripts in this course.


#### _Circling Back on HDFS_
Since Spark does not have its own distributed storage system, it leverages using `HDFS` or `AWS S3`, or any other distributed storage. Primarily in this course, we will be using AWS S3. 

#### _MapReduce System_
* HDFS uses MapReduce system as a resource manager to allow the distribution of the files across the **hard drives** within the cluster. 
* Spark, on the other hand, runs the operations and holds the data in the **RAM memory** rather than the hard drives used by HDFS. 

_Since Spark lacks a file distribution system to organize, store and process data files, Spark tools are often installed on Hadoop because Spark can then use the Hadoop Distributed File System (HDFS)._

#### _Why Would You Use an EMR Cluster?_
* Since a Spark cluster includes multiple machines, in order to use Spark code on each machine, we would need to download and install Spark and its dependencies. 
* AWS EMR negates the need users to go through the manual process of installing Spark and its dependencies for each machine.


**Quiz Question**

_What are some characteristics of the AWS EMR standalone mode?_
* AWS EMR standalone mode is both distributed and a resource manager.

___ 

### Introduction to AWS Glue

#### Glue Studio 

* Glue is an AWS Service that relies on Spark. 
* we can use Glue Studio to write purely Spark scripts.

Using AWS Glue to run Spark Jobs requires the following resources and configuration:

<img src="../L4-using-spark-in-aws/images/2-aws_glue_config.png" width=70% height=70%>

##### Routing Table
* an entity that stores the network paths to various locations
* e.g.: will store the path to S3 from within your VPC
* will need a routing table to configure with your VPC Gateway

##### VPC Gateway
* cloud project runs resources within a Virtual Private Cloud (VPC)
* i.e. Glue Job runs in a Secure Zone without access to anything outside your Virtual Network
* a network entity gives access to outside networks and resources since S3 is a shared service and doesn't reside in VPC

##### S3 Gateway Endpoint
* by default, Glue Jobs can't reach any networks outside of VPC
* since S3 runs in different network, we need to create an S3 Gateway Endpoint
* it allows S3 traffic from your Glue Jobs into your S3 buckets
* once created the endpoint, Glue Jobs will have a network path to reach S3

##### S3 Buckets
* buckets are storage locations within AWS, that have a hierarchical directory-like structure. 
* the bucket is the "parent" of all the sub-directories and files