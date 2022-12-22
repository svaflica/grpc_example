import grpc_out.service_pb2_grpc as service_grpc
import grpc_out.service_pb2 as service

class Tokenizer(service_grpc.TokenizerServicer):
    def get_tokens(self, request, context):
        text = request.text
        tokens = text.split(' ')
        response = service.Response()
        response.listOfStrings.extend(tokens)
        return response
