
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator

with DAG(
    dag_id='Pizza2Postgres_dev',
    default_args={'owner': 'airflow'},
    schedule_interval='@daily',
    start_date=days_ago(1)
) as dag:

    airbyte_sync = AirbyteTriggerSyncOperator(
        task_id='airbyte_sync_example',
        airbyte_conn_id='AirbyteConnection',
        connection_id='440b278b-1b35-495e-9463-e06b5706bd04',
        asynchronous=False,
        timeout=3600,
        wait_seconds=3
    )



# from airflow import DAG
# from airflow.utils.dates import days_ago
# from airflow.providers.airbyte.operators.airbyte import AirbyteTriggerSyncOperator
# from pendulum import datetime

# with DAG(dag_id='trigger_airbyte_job_example',
#          default_args={'owner': 'airflow'},
#          schedule_interval='@daily',
#         #  start_date=days_ago(1)
#          start_date=datetime(2024, 1, 1),
#     ) as dag:

#     money_to_json = AirbyteTriggerSyncOperator(
#         task_id='airbyte_money_json_example',
#         airbyte_conn_id='AirbyteConnection',
#         connection_id='45946a38-bcd1-4237-b5d9-6b47240ee2ab',
#         asynchronous=True,
#         timeout=3600,
#         wait_seconds=3
#     )