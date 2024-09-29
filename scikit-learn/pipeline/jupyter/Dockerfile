FROM jupyter/base-notebook:python-3.10.6

USER root

COPY ./requirements.txt /home/jovyan/requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /home/jovyan/requirements.txt

USER jovyan

WORKDIR /home/jovyan/work


