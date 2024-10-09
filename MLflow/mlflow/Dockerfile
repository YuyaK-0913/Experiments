FROM python:3.10-slim

WORKDIR /opt
# RUN mkdir -p /opt/outputs/mlruns
RUN pip install mlflow sqlalchemy psycopg2-binary google-cloud-storage azure-storage-blob boto3

CMD [ "mlflow", "server", "--backend-store-uri", "/opt/outputs", "--default-artifact-root", "/opt/outputs", "--host", "0.0.0.0" ]
