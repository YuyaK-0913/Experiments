FROM python:3.10.6-slim

WORKDIR /app

COPY ../client /app
COPY ../proto /app/proto

RUN pip install grpcio grpcio-tools protobuf

RUN python -m grpc_tools.protoc -I./proto --python_out=./proto --grpc_python_out=./proto ./proto/helloworld.proto

# # ビルド時にコマンドを実行する場合
# RUN python -m client

# # コンテナ起動時にコマンドを実行する場合
CMD ["python", "-m", "client"] 
# CMD ["python", "client.py"] 
