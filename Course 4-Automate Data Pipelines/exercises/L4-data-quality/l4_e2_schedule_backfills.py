# Instructions
# 1 - Revisit our bikeshare traffic
# 2 - Update our DAG with
#  a - @monthly schedule_interval
#  b - max_active_runs of 1
#  c - start_date of 2018/01/01
#  d - end_date of 2018/02/01
# Use Airflow’s backfill capabilities to analyze our trip data on a monthly basis over 2 historical runs

# Remember to run "/opt/airflow/start.sh" command to start the web server. Once the Airflow web server is ready,  open the Airflow UI using the "Access Airflow" button.
# Turn your DAG “On”, and then Run your DAG. If you get stuck, you can take a look at the solution file in the workspace/airflow/dags folder in the workspace and the video walkthrough on the next page.

import pendulum

from airflow.decorators import dag, task
from airflow.secrets.metastore import MetastoreBackend
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.python_operator import PythonOperator

from udacity.common import sql_statements


@dag(
    start_date=pendulum.datetime(2018, 1, 1, 0, 0, 0, 0),
    # TODO: Set the end date to February first
    end_date=pendulum.datetime(2018, 2, 1, 0, 0, 0, 0),
    # TODO: Set the schedule to be monthly
    schedule_interval='@monthly',
    # TODO: set the number of max active runs to 1
    max_active_runs=1
)
def schedule_backfills():

    @task()
    def load_trip_data_to_redshift(*args, **kwargs):
        metastoreBackend = MetastoreBackend()
        aws_connection = metastoreBackend.get_connection("aws_credentials")

        redshift_hook = PostgresHook("redshift")
        sql_stmt = sql_statements.COPY_ALL_TRIPS_SQL.format(
            aws_connection.login,
            aws_connection.password,
        )
        redshift_hook.run(sql_stmt)

    @task()
    def load_station_data_to_redshift(*args, **kwargs):
        metastoreBackend = MetastoreBackend()
        aws_connection = metastoreBackend.get_connection("aws_credentials")
        redshift_hook = PostgresHook("redshift")
        sql_stmt = sql_statements.COPY_STATIONS_SQL.format(
            aws_connection.login,
            aws_connection.password,
        )
        redshift_hook.run(sql_stmt)

    create_trips_table = PostgresOperator(
        task_id="create_trips_table",
        postgres_conn_id="redshift",
        sql=sql_statements.CREATE_TRIPS_TABLE_SQL
    )

    create_stations_table = PostgresOperator(
        task_id="create_stations_table",
        postgres_conn_id="redshift",
        sql=sql_statements.CREATE_STATIONS_TABLE_SQL,
    )

    load_trips_task = load_trip_data_to_redshift()
    load_stations_task = load_station_data_to_redshift()

    create_trips_table >> load_trips_task
    create_stations_table >> load_stations_task


schedule_backfills_dag = schedule_backfills()
