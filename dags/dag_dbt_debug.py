from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import days_ago

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

# Define the DAG
with DAG(
    'dbt_debug_dag',
    default_args=default_args,
    description='A simple DAG to run dbt debug with a target parameter',
    schedule_interval=None,  # This DAG will not be scheduled
) as dag:

    # Define the dbt debug command as a BashOperator
    run_dbt_debug = BashOperator(
        task_id='run_dbt_debug',
        bash_command='dbt debug --target {{ params.target }}',
        params={'target': 'dev'},  # Default target
    )
