from datetime import datetime

from airflow.sdk import DAG, task


with DAG(
    dag_id="test_hello_dag",
    description="Smoke test DAG for the local Airflow setup",
    schedule="@daily",
    start_date=datetime(2026, 4, 1),
    catchup=False,
    tags=["test"],
) as dag:
    @task
    def say_hello() -> str:
        message = "hello from airflow-etlers"
        print(message)
        return message

    say_hello()
