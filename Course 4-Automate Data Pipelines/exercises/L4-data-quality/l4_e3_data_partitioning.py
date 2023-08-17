# Instructions
# 1 - Retrieve the execution_date from kwargs
# 2 - Modify the bikeshare DAG to load data month by month, instead of loading it all at once, every time.

import pendulum


from airflow.decorators import dag, task
from airflow.secrets.metastore import MetastoreBackend
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.postgres_operator import PostgresOperator

from udacity.common import sql_statements


@dag(
    start_date=pendulum.datetime(2018, 1, 1, 0, 0, 0, 0),
    end_date=pendulum.datetime(2018, 2, 1, 0, 0, 0, 0),
    schedule_interval='@monthly',
    max_active_runs=1
)
def data_partitioning():

    @task()
    def load_trip_data_to_redshift(*args, **kwargs):
        metastoreBackend = MetastoreBackend()
        aws_connection = metastoreBackend.get_connection("aws_credentials")
        redshift_hook = PostgresHook("redshift")
        # # #
        # TODO: How do we get the execution_date from our context?
        # execution_date=kwargs["<REPLACE>"]
        execution_date = kwargs["execution_date"]
        # # #

        # # #
        # TODO: modify the parameters when formatting sql_statements.COPY_ALL_TRIPS_SQL
        # to include the year and month the pipeline executed
        #

        sql_stmt = sql_statements.COPY_MONTHLY_TRIPS_SQL.format(
            aws_connection.login,
            aws_connection.password,
            year=execution_date.year,  # extract just the year that we were looking for
            month=execution_date.month  # extract just the month that we were looking for
        )
        redshift_hook.run(sql_stmt)

    load_trip_data_to_redshift_task = load_trip_data_to_redshift()

    @task()
    def load_station_data_to_redshift():
        metastoreBackend = MetastoreBackend()
        aws_connection = metastoreBackend.get_connection("aws_credentials")
        redshift_hook = PostgresHook("redshift")
        sql_stmt = sql_statements.COPY_STATIONS_SQL.format(
            aws_connection.login,
            aws_connection.password,
        )
        redshift_hook.run(sql_stmt)

    load_station_data_to_redshift_task = load_station_data_to_redshift()

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

    create_trips_table >> load_trip_data_to_redshift_task
    create_stations_table >> load_station_data_to_redshift_task


data_partitioning_dag = data_partitioning()
