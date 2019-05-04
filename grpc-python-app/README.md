
## Password generator web app using grpc

### Steps:
1. run `python3 -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/service.proto`
2. run server with `python3 server.py`
3. run client with `python3 client.py --base <base_password> --key <my_key>`. Both arguments are optional


### Prerequisites:
* Make sure you have `grpcio-tools` installed. If not use `pip3 install grpcio-tools` to do so