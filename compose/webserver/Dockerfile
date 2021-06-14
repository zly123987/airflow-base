FROM puckel/docker-airflow:1.10.9

#ENV PYTHONUNBUFFERED 1

# Install requirements
USER root
COPY requirements/webserver.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt \
    && rm -f /requirements.txt

#RUN usermod -aG sudo airflow
#USER airflow

#ENV PYTHONHASHSEED 1
