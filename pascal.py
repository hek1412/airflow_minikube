from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
from datetime import datetime

def generate_and_print_pascals_triangle(n):
    triangle = []
    for row_num in range(n):
        row = [1] * (row_num + 1)
        for j in range(1, row_num):
            row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
        triangle.append(row)
    
    max_width = len(" ".join(map(str, triangle[-1])))
    for row in triangle:
        row_str = " ".join(map(str, row))
        print(row_str.center(max_width))

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 11, 17),
    'email_on_failure': False,
    'email_on_retry': False,
}

dag = DAG('pascal', default_args=default_args, schedule_interval='@daily')

start = DummyOperator(
    task_id='start',
    dag=dag,
)

end = DummyOperator(
    task_id='end',
    dag=dag,
)

python_task = PythonOperator(
    task_id='print_pascals_triangle',
    python_callable=print_pascals_triangle,
    op_args=[10],
    dag=dag,
)

start >> python_task >> end
