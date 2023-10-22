import grpc
from concurrent import futures
import proconnectx_pb2
import proconnectx_pb2_grpc

_USERS = {}

class ProConnectXServicer(proconnectx_pb2_grpc.ProConnectXServicer):

    def Register(self, request, context):
        username = request.username
        password = request.password
        if username in _USERS:
            return proconnectx_pb2.RegistrationResponse(success=False, message="Username already exists.")
        _USERS[username] = password
        return proconnectx_pb2.RegistrationResponse(success=True, message="Registration successful.")

    def Login(self, request, context):
        username = request.username
        password = request.password
        if username not in _USERS or _USERS[username] != password:
            return proconnectx_pb2.LoginResponse(success=False, message="Invalid username or password.", user_id=0)
        return proconnectx_pb2.LoginResponse(success=True, message="Login successful.", user_id=1)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    proconnectx_pb2_grpc.add_ProConnectXServicer_to_server(ProConnectXServicer(), server)
    server.add_insecure_port('localhost:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()