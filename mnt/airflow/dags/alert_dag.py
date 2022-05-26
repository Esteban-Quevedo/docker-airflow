from airflow import DAG
from airflow.operators.bash_operator import BashOperator

from datetime import datetime, timedelta

default_args = {
    'start_date': datetime(2022, 3, 23),
    'owner': 'Airflow',
    'retries': 3,
    'retry_delay': timedelta(seconds=60),
    'emails': ['email1@airflow.com', 'email2@airflow.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'email': "email1@airflow.com",
}

def on_success_dag(dict):
    print("on_success_dag")
    print(dict)

def on_failure_dag(dict):
    print("on_failure_dag")
    print(dict)

with DAG(dag_id='alert_dag', schedule_interval="0 0 * * *", default_args=default_args, catchup=True,  dagrun_timeout=timedelta(seconds=75), on_success_callback=on_success_dag, on_failure_callback=on_failure_dag) as dag:

    # Task 1
    t1 = BashOperator(task_id='t1', bash_command="echo 'first task'")

    # Task 2
    t2 = BashOperator(task_id='t2', bash_command="echo 'second task'")

    t1 >> t2