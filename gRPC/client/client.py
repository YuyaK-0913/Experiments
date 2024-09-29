import grpc
import proto.helloworld_pb2 as helloworld_pb2
import proto.helloworld_pb2_grpc as helloworld_pb2_grpc

def run():
    channel = grpc.insecure_channel('server:50051')
    stub = helloworld_pb2_grpc.GreeterStub(channel)
    name = "World"
    response = stub.SayHello(helloworld_pb2.HelloRequest(name=name))
    print("Client received: " + response.message)

if __name__ == '__main__':
    run()
