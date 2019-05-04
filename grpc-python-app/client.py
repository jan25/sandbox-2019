import grpc
import service_pb2_grpc
import service_pb2
import argparse

argparser = argparse.ArgumentParser()
argparser.add_argument('--base', help='base password')
argparser.add_argument('--key', help='encryption key')

args = argparser.parse_args()
base_password = args.base or 'password'
key = int(args.key or 0)

channel = grpc.insecure_channel('localhost:50051')
stub = service_pb2_grpc.PasswordGeneratorStub(channel)

password_request = service_pb2.PasswordRequest(
    basePassword=base_password,
    encryptionKey=key
)
password = stub.GeneratePassword(password_request)
print (password.password)