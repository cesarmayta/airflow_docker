from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator

def saludo():
    print("hola mundo")

with DAG(
    dag_id="prueba_hola_mundo",
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=["ejemplo"],
    schedule="@daily"
) as dag:
    imprimir_hola = PythonOperator(
        task_id="imprimir_hola_mundo",
        python_callable=saludo,
    )