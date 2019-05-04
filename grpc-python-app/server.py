import service_pb2_grpc
import service_pb2
import grpc
import concurrent.futures
import time
import logging

_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class PasswordGeneratorServicer(service_pb2_grpc.PasswordGeneratorServicer):
    '''
    Generated method from protoc
    uses grpcio-tools generated py modules as argument, return types
    '''
    def GeneratePassword(self, request, context):
        base_password = request.basePassword
        encryption_key = request.encryptionKey
        return service_pb2.GeneratedPassword(
            password=self.actuallyGeneratePassword(base_password, encryption_key)
        )

    '''
    Actually generated a password based on supplied:
    base_password: string
    key: int
    This is a pure function, it rotates a window of password forwards and
    rest of password backwards based on given key. Nice, huh?
    Returns
    ----
    password: string
    '''
    def actuallyGeneratePassword(self, base_password, key=13):
        key = abs(key) % 26 # Just to make sure we are in range of alphabets
        n = len(base_password)
        forward_window_size = n // 3
        window_start_idx = key % n
        window_end_idx = (window_start_idx + forward_window_size) % n
        password = []
        if window_end_idx >= window_start_idx:
            password = self.rotateStr(base_password[:window_start_idx], -1 * key)
            password += self.rotateStr(base_password[window_start_idx:window_end_idx], key)
            password += self.rotateStr(base_password[window_end_idx:], -1 * key)
        else:
            password = self.rotateStr(base_password[:window_end_idx], key)
            password += self.rotateStr(base_password[window_end_idx:window_start_idx], -1 * key)
            password += self.rotateStr(base_password[window_start_idx:], key)
        return ''.join(password)
    
    def rotateStr(self, s, by):
        return ''.join([chr(ord('a') + (ord(c) - ord('a') + by + 26) % 26) for c in s])

def serve():
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_PasswordGeneratorServicer_to_server(
        PasswordGeneratorServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

serve()