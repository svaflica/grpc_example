from concurrent import futures

import grpc

import grpc_out.service_pb2_grpc as service_grpc

from server.server import Tokenizer

port = '50051'
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
service_grpc.add_TokenizerServicer_to_server(Tokenizer(), server)
server.add_insecure_port('[::]:' + port)
server.start()
print("Server started, listening on " + port)
server.wait_for_termination()