FROM quay.io/astronomer/astro-runtime:10.0.0

# replace dbt-postgres with another supported adapter if you're using a different warehouse type
RUN python -m venv dbt_venv && source dbt_venv/bin/activate && \
    pip install --no-cache-dir dbt-postgres dbt-core && deactivate


# FROM apache/airflow:2.8.0
ENV AIRFLOW__CORE__TEST_CONNECTION=Enabled