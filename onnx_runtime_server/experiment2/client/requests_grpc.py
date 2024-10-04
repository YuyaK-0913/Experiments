import requests

import numpy as np
from google.protobuf.json_format import MessageToJson

import grpc
from proto import onnx_ml_pb2, predict_pb2, prediction_service_pb2_grpc

from typing import List


# data = np.array([1, 2, 3, 4, 5], dtype=np.float32)
data = np.arange(64).reshape(1, 64).astype(np.float32)

# serving_address = "client:50051"
serving_address = "localhost:50051"  # DockerコンテナのIP

onnx_input_name = "float_input"
onnx_output_name = "variable"

channel = grpc.insecure_channel(serving_address)
stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)


input_tensor = onnx_ml_pb2.TensorProto()
input_tensor.dims.extend(data.shape)
input_tensor.data_type = 1
input_tensor.raw_data = data.tobytes()

request_message = predict_pb2.PredictRequest()
request_message.inputs[onnx_input_name].data_type = input_tensor.data_type
request_message.inputs[onnx_input_name].dims.extend(data.shape)
request_message.inputs[onnx_input_name].raw_data = input_tensor.raw_data

response = stub.Predict(request_message)
output = np.frombuffer(response.outputs[onnx_output_name].raw_data, dtype=np.float32)

print(output)