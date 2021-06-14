""" Workflow definitions for RSS update of Packagist and Pypi libs.
    When deploying, please ensure that the Db conf file for the pipeline
    is created in ../submodules/library-pipeline/config/configuration.ini
"""

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

queue = "aws"


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2018, 12, 21, 18, 0, 0),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    "queue": queue,
}

dag = DAG(
    "example_dag",
    default_args=default_args,
    schedule_interval=timedelta(minutes=10),
)

example_task = BashOperator(
    task_id="example_task",
    provide_context=True,
    bash_command="""
            echo "Scantist Number One"
    """,
    dag=dag,
)

example_task_2 = BashOperator(
    task_id="example_task_2",
    provide_context=True,
    bash_command="""
            echo "Everyone loves Scantist"
    """,
    dag=dag,
)
example_task >> example_task_2
