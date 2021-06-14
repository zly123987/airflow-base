FROM puckel/docker-airflow:1.10.9

ENV PYTHONUNBUFFERED 1


ARG AIRFLOW_HOME
ENV AIRFLOW_HOME=$AIRFLOW_HOME

# Install Java 8 - no longer officially available on Debian 10
# But Spark 2.3.3 + Scala_11 requires Java 8
# Workaround: https://linuxize.com/post/install-java-on-debian-10/
USER root
RUN apt-get update \
    && apt-get upgrade -y \
    && apt-get -y install sudo \

RUN usermod -aG sudo airflow
USER airflow

ENV PYTHONHASHSEED 1
