import grpc
import grpc_out.service_pb2_grpc as service_grpc
import grpc_out.service_pb2 as service

with grpc.insecure_channel('localhost:50051') as channel:
    stub = service_grpc.TokenizerStub(channel)
    response = stub.get_tokens(service.Request(text='Mother Fathr Brother'))
    print("Tokens: ", response.listOfStrings)