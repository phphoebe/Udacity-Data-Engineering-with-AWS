# Course 3 - Spark and Data Lakes
Learn about the big data ecosystem and how to use Spark to work with massive datasets. 
Learn about how to store big data in a data lake and query it with Spark

## [Lesson 1 - Introduction to Spark and Data Lakes](https://github.com/phphoebe/Udacity-Data-Engineering-with-AWS/blob/main/Course%203-Spark%20and%20Data%20Lakes/L2-Big%20Data%20Ecosystem/notes.md)
Learn how Spark evaluates code and uses distributed computing to process and transform data. Work in the big data ecosystem to build data lakes and data lakehouses. 

## [Lesson 2 - Big Data Ecosystem, Data Lakes & Spark](https://github.com/phphoebe/Udacity-Data-Engineering-with-AWS/tree/main/Course%203-Spark%20and%20Data%20Lakes/L2-Big%20Data%20Ecosystem)
Learn about the problems that Apache Spark is designed to solve. Learn about the greater Big Data ecosystem and how Spark fits into it. 
* Identify what consititues the big data ecosystem for data engineering 
* Explain the purpose and evolution of data lakes in the big data ecosystem 
* Compare the Spark framework with Hadoop framework 
* Identify when to use Spark and when not to use it
* Describe the features of lakehouse architecture 

## Lesson 3 - Spark Essentials 
Dive into how to use Spark for wrangling, filtering, and transforming distributed data with PySpark and Spark SQL 
* Wrangle data with Spark and functional programming to scale across distributed systems
* Process data with Spark DataFrames and Spark SQL
* Process data in common formats such as CSV and JSON
* Use the Spark RDDs API to wrangle data 
* Transform and filter data with Spark

## Lesson 4 - Using Spark in AWS
Learn to use Spark and work with data lakes with Amazon Web Services using S3, AWS Glue, and AWS Glue Studio 
* Use distributed data storage with Amazon S3
* Identify properties of AWS S3 data lakes
* Identify service options for using Spark in AWS 
* Configure AWS Glue
* Create and run Spark Jobs with AWS Glue
## Lesson 5 - Ingesting and Organizing Data in a Lakehouse 
Work with Lakehouse zones. Build and configure these zones in AWS. 
* Use Spark with AWS Glue to run ELT processes on data of diverse sources, structures, and vintages in lakehouse architecture
* Create a Glue Data Catalog and Glue Tables
* Use AWS Athena for ad-hoc queries in a lakehouse 
* Leverage Glue for SQL AWS S3 queries and ELT
* Ingest data into lakehouse zones
* Transform and filter data into curated lakehouse zones with Spark and AWS Glue
* Join and process data into lakehouse zones with Spark and AWS Glue


## Project - STEDI Human Balance Analytics 
Work with sensor data that trains a machine learning model. Load S3 JSON data from a data lake into Athena tables using Spark and AWS Glue. 

---

# PySpark Installation

* install Java using [Homebrew](https://formulae.brew.sh/formula/openjdk@11)

  ```
  brew install openjdk@11
  ```
* for the system Java wrappers to find this JDK, symlink it with
  ```
  sudo ln -sfn $HOMEBREW_PREFIX/opt/openjdk@11/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-11.jdk
  ```
  
* create a virtual environment
  ```
  python3 -m venv spark-test
  ```

* activate the virtual env
  ```
  source spark-test/bin/activate
  ```
  
* install PySpark 
  ```
  pip install pyspark
  ```
  
## Setup PySpark and Jupyter Notebook

* install in the `spark-test` virtual env
  ```
  pip install jupyterlab
  pip install ipykernel
  ```
  
* register the new virtual env with Jupyter so that you can use it within JupyterLab
  ```
  python3 -m ipykernel install --user --name='spark-test'
  ```
  
Now open an existing/create a new `.ipynb` file in VS Code and select the `spark-test` Kernel to use
