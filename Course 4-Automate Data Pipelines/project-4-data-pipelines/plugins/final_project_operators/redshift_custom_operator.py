# Custom Operator to execute multiple SQL statements in SQL file in Redshift
# Reference: https://blog.shellkode.com/airflow-postgresql-operator-to-execute-multiple-sql-statements-dd0d07365667

from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.models.baseoperator import BaseOperator
from airflow.utils.decorators import apply_defaults


class PostgreSQLOperator(BaseOperator):
    template_fields = ('sql')
    template_fields_renderers = {'sql': 'sql'}
    template_ext = ('.sql')
    ui_color = '#99e699'

    @apply_defaults
    def __init__(self,
                 *,
                 sql: str = '',
                 postgres_conn_id: str = 'postgres_default',
                 autocommit: bool = True,
                 **kwargs,
                 ) -> None:
        super().__init__(**kwargs)
        self.sql = sql
        self.postgres_conn_id = postgres_conn_id
        self.autocommit = autocommit

    def execute(self, context) -> None:
        postgres_hook = PostgresHook(postgres_conn_id=self.postgres_conn_id)
        """
        Executes SQL Statements on Redshift cluster
        """
        try:
            postgres_hook.run(self.sql, self.autocommit) if isinstance(self.sql, str) else [
                postgres_hook.run(query, self.autocommit) for query in self.sql]
            self.log.info('SQL Query Execution complete!')

        except Exception as e:
            raise
