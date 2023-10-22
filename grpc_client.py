import grpc
import proconnectx_pb2
import proconnectx_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = proconnectx_pb2_grpc.ProConnectXStub(channel)
        print("Registration")
        response = stub.Register(proconnectx_pb2.RegistrationRequest(username="test", password="password"))
        print("Registration Status:", response.success, response.message)

        print("Login")
        response = stub.Login(proconnectx_pb2.LoginRequest(username="test", password="password"))
        print("Login Status:", response.success, response.message, response.user_id)

if __name__ == '__main__':
    run()