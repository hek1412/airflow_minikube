#                             Certification 1T (DevOps)
## Задание 8. Развертывание Apache Airflow в Minikube и создание простого DAG

Это DAG **(my-dag.py**) с использованием BashOperator и PythonOperator. 

BashOperator выводит "Текущее время", PythonOperator выводит время безотказной работы системы в минутах.

После развертывания Airflow в Minikube с базовыми настройками, ждем готовности подов:
```
helm install airflow apache-airflow/airflow --debug --namespace airflow --create-namespace --set dags.gitSync.enabled=true --set dags.gitSync.repo=https://github.com/hek1412/airflow_minikube.git --set dags.gitSync.branch=main --set dags.gitSync.subPath="/" 
```
![Результат установки.](/1.png)

Открываем веб-интерфейс Airflow и запускаем DAG * my_dag *

![Запуск DAG.](/2.png)

Убедимся, что все выполнено, смотрим логи каждого оператора (bash_task и print_uptime_task)

![Логи BashOperator.](/3.png)
![Логи PythonOperator.](/4.png)

Возвращаемся в Терминал и проверяем правильность работы операторов
```
date
```
```
uptime -p
```

ПОБЕДА, DAG не обманул!!!)

![uptime -p.](/5.png)

*В файле pascal.py выполняется реализация треугольника паскаля в DAG по занятию 6.7.2
(Время запуска - 11:44. Запуск - ежедневный.)*
