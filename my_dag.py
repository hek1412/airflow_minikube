from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import subprocess

# Определяем Python-функцию, которую будем вызывать предназначена для получения и отображения времени безотказной работы системы (uptime)
def print_uptime():
    try:
        result = subprocess.run(['uptime', '-p'], capture_output=True, text=True)
        uptime = result.stdout.strip()
        # Форматирование
        formatted_uptime = '. '.join(uptime.split(', '))
        print(f"\nТекущее время безотказной работы составляет:\n... {formatted_uptime} ...\n")
        
    except Exception as e:
        print(f"Ошибка: {str(e)}")

# Задаем параметры DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 11, 18, 9, 45, 0),  # Убедитесь, что дата не в будущем
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

# Создаем DAG
with DAG(
    'my_dag',
    default_args=default_args,
    description='DAG с Bash и Python операторами',
    schedule_interval='@daily',
    catchup=False,
) as dag:

    # Создаем задачу с использованием BashOperator
    bash_task = BashOperator(
        task_id='bash_task',
        bash_command='echo "Текущее время: $(date)"',  # Правильный bash синтаксис
    )

    # Создаем задачу с использованием PythonOperator
    uptime_task = PythonOperator(
        task_id='print_uptime_task',
        python_callable=print_uptime,
    )

    # Определяем последовательность выполнения задач
    bash_task >> uptime_task
