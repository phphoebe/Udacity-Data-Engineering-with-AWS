import pendulum
from datetime import timedelta

from airflow.decorators import dag
from airflow.operators.dummy_operator import DummyOperator
from final_project_operators.redshift_custom_operator import PostgreSQLOperator

default_args = {
    'owner': 'Phoebe',
    'start_date': pendulum.now(),
    'depends_on_past': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'catchup': False,
    'email_on_retry': False
}


@dag(
    default_args=default_args,
    description='Create tables in Redshift with Airflow',
    schedule_interval='0 * * * *'
)
def create_tables():
    start_operator = DummyOperator(task_id='Begin_execution')

    create_redshift_tables = PostgreSQLOperator(
        task_id='Create_tables',
        postgres_conn_id='redshift',
        sql='create_tables.sql'
    )

    end_operator = DummyOperator(task_id='Stop_execution')

    start_operator >> create_redshift_tables >> end_operator


create_tables_dag = create_tables()
