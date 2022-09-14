import time

import grpc
import proto.adapter_pb2_grpc as rpc
import proto.adapter_pb2 as service_entities

class Client:
    def __init__(self, address: str = 'localhost:11111'):
        channel = grpc.insecure_channel(address)
        self.connection = rpc.AdapterStub(channel)

    def get_depth(self):
        return self.connection.get_depth(request=service_entities.Empty())


if __name__ == "__main__":
    c = Client()
    while 1:
        depth = c.get_depth()
        print(int(time.time()*1000),depth.timestamp, int(time.time()*1000) - depth.timestamp)
        time.sleep(0.1)