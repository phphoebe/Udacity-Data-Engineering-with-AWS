# Course 4 - Automate Data Pipelines
Build pipelines leveraging Airflow DAGs to organize your tasks along with AWS resources such as S3 and Redshift 

## Lesson 1 - Data Pipelines 
Learn about the components of a data pipeline including Directed Acyclic Graphs (DAGs). Practice creating data pipelines with DAGs and Apache Airflow.
* Define and describe a data pipeline and its usage
* Explain the relationship between DAGs, S3, and Redshift with a given example
* Employ tasks as instantiated operators
* Organize task dependencies based on logic flow
* Apply templating in codebase with kwargs parameter to set runtime variables

## Lesson 2 - Airflow and AWS 
Creates connections between Airflow and AWS first by creating credentials, then copying S3 data, leveraging connections and hooks, and building S3 data to the Redshift DAG. 
* Create Airflow Connection to AWS using AWS credentials 
* Create Postgres/Redshift Airflow Connections
* Leverage hooks to use Connections in DAGs
* Connect S3 to Redshift DAG programmatically 

## Lesson 3 - Data Quality 
Learn how to track data lineage and set up data pipeline schedules, partition data to optimize pipelines, investigating Data Quality issues, and write tests to ensure data quality. 
* Utilize the logic flow of task dependencies to investigage potential erros within data lineage
* Leverage Airflow catchup to backfill data 
* Extract data from a specific time range by employing the kwargs parameters 
* Create a task to ensure data quality within select tables 

## Lesson 4 - Production Data Pipelines 
Learn how to build Pipelines with maintainability and resuability in mind. Also learn about pipeline monitoring. 
* Consolidate repeated code into operator plugins 
* Refactor a complex task into multiple tasks with separate SQL statements 
* Convert an Airflow 1 DAG into an Airflow 2 DAG
* Construct a DAG and custom operator end-to-end


## Project - Data Pipelines 
Work on a music streaming company's data infrastructure by creating and automating a set of data pipelines with Airflow, monitoring and debugging production pipelines.
