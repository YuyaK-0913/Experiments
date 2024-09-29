FROM python:3.10.6-slim

WORKDIR /app

COPY ../server /app
COPY ../proto /app/proto

RUN pip install grpcio grpcio-tools protobuf

RUN python -m grpc_tools.protoc -I./proto --python_out=./proto --grpc_python_out=./proto ./proto/helloworld.proto

EXPOSE 50051

# # ビルド時にコマンドを実行する場合
# RUN python -m server

# # コンテナ起動時にコマンドを実行する場合
CMD ["python", "-m", "server"] 
# CMD ["python", "server.py"] 

