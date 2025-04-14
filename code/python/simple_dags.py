from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator
from datetime import datetime, timedelta

# with DAG(
#     dag_id="simple_dag",
#     start_date=datetime(2025, 1, 1),
#     schedule_interval="@daily",
#     catchup=False,
# ) as dag:
#     start = BashOperator(
#         task_id="start_task",
#         bash_command="echo 'Starting the workflow!'",
#     )
#     end = BashOperator(
#         task_id="end_task",
#         bash_command="echo 'Workflow complete!'",
#     )
#     start >> end

# with DAG(
#     dag_id="etl_dag",
#     start_date=datetime(2025, 1, 1),
#     schedule_interval="@daily",
#     catchup=False,
# ) as dag:
#     extract = BashOperator(task_id="extract", bash_command="echo 'Extractiong data'")
#     transform = BashOperator(
#         task_id="transform", bash_command="echo 'Transforming data'"
#     )
#     load = BashOperator(task_id="load", bash_command="echo 'Loading date'")

#     extract >> transform >> load


# def process_data():
#     print("Processing data with Python!")


# with DAG(
#     dag_id="python_dag",
#     start_date=datetime(2025, 1, 1),
#     schedule_interval="@daily",
#     catchup=False,
# ) as dag:
#     start = PythonOperator(task_id="start", python_callable=process_data)


# with DAG(
#     dag_id="complex_dag",
#     start_date=datetime(2025, 1, 1),
#     schedule_interval="@daily",
#     catchup=False,
# ) as dag:
#     extract = BashOperator(task_id="extract", bash_command="echo 'Extract'")
#     transform1 = BashOperator(task_id="transform1", bash_command="echo 'Transform 1'")
#     transform2 = BashOperator(task_id="transform2", bash_command="echo 'Transform 2'")
#     load = BashOperator(task_id="load", bash_command="echo 'Load'")
#     extract >> [transform1, transform2] >> load


# default_args = {
#     "retries": 2,
#     "retry_delay": timedelta(minutes=2),
# }

# with DAG(
#     dag_id="param_dag",
#     start_date=datetime(2025, 4, 13),
#     schedule_interval="@daily",
#     catchup=False,
#     max_active_runs=2,
#     default_args=default_args,
#     description="A daily workflow with custom paramters",
# ) as dag:
#     start = BashOperator(task_id="start_task", bash_command="echo 'Staring!'")
#     end = BashOperator(task_id="end_stask", bash_command="echo 'Done!'")
#     start >> end


# with DAG(
#     dag_id="cwd_bash_dag",
#     start_date=datetime(2025, 4, 1),
#     schedule_interval="@daily",
#     catchup=False,
# ) as dag:
#     run_cwd = BashOperator(
#         task_id="run_cwd",
#         bash_command="ls -l",
#         cwd="/tmp",
#     )

# with DAG(
#     dag_id="exit_code_bash_dag",
#     start_date=datetime(2025, 4, 1),
#     schedule_interval="@daily",
#     catchup=False,
# ) as dag:
#     run_exit = BashOperator(
#         task_id="run_exit",
#         bash_command="exit 100",
#         skip_exit_code=100,
#     )


# def afternoon_task():
#     print("Running at 2:30 PM!")


# with DAG(
#     dag_id="specific_time_dag",
#     start_date=datetime(2025, 1, 1),
#     schedule_interval="15 * * * *",  # 2:30 PM daily
#     catchup=False,
# ) as dag:
#     task = PythonOperator(
#         task_id="afternoon_task",
#         python_callable=afternoon_task,
#     )


# def catchup_task(ds):
#     print(f"Processing data for {ds}")


# with DAG(
#     dag_id="catchup_daily_dag",
#     start_date=datetime(2025, 4, 9),
#     schedule_interval="0 0 * * *",  # Midnight UTC daily
#     catchup=True,
# ) as dag:
#     task = PythonOperator(
#         task_id="catchup_task",
#         python_callable=catchup_task,
#         op_kwargs={"ds": "{ { ds } }"},
#     )


def banch_func(**context):
    excution_date = context["execution_date"]
    print(excution_date)
    if excution_date.weekday() < 5:
        return "weekday_task"
    else:
        return "weekend_task"


with DAG(
    dag_id="banching_dag",
    start_date=datetime(2025, 4, 14),
    schedule_interval="@daily",
    catchup=False,
) as dag:
    branch_task = BranchPythonOperator(
        task_id="branch_task",
        python_callable=banch_func,
        provide_context=True,
    )
    weekday_task = BashOperator(
        task_id="weekday_task",
        bash_command="echo 'Running on a weekday!'",
    )
    weekend_task = BashOperator(
        task_id="weekend_task",
        bash_command="echo 'Running on a weekend!'",
    )

    branch_task >> [weekday_task, weekend_task]
