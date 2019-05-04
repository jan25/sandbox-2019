import grpc
import service_pb2_grpc
import service_pb2

channel = grpc.insecure_channel('localhost:50051')
stub = service_pb2_grpc.PasswordGeneratorStub(channel)

password_request = service_pb2.PasswordRequest()
password = stub.GeneratePassword()