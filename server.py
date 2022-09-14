import logging
import time
import grpc
from concurrent import futures

import config
import proto.adapter_pb2 as service
import proto.adapter_pb2_grpc as rpc
from config import EXCHANGE_CLASS, EXCHANGE_CREDETIANS
import threading
import atexit
import definitions

logging.basicConfig(filename="proxy_{0}.txt".format(time.strftime("%d-%m-%Y_%H_%M_%S", time.localtime())))
logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger().addHandler(logging.StreamHandler())



@atexit.register
def goodbye():
    logging.info("I received SIGINT. Bye.")
    exit(-1)


exchange = EXCHANGE_CLASS(EXCHANGE_CREDETIANS)
lock = threading.Lock()
order_book = {}


def depth_timestamp_checker():
    while 1:
        try:
            with lock:
                timestamp = order_book["last_update"]
        except:
            pass
        time.sleep(definitions.DELAY_BETWEEN_TIMESTAMP_CHECKS)


class Server(rpc.AdapterServicer):
    def __init__(self, exchange):
        self.exchange = exchange
        pass

    def get_depth(self, request, context):
        # global order_book
        with lock:
            if len(order_book) == 0:
                return service.Depth(bids=[], asks=[], timestamp=-1, error="Orderbook is empty")
            bids = []
            for i in order_book["bids"]:
                bids.append(service.DepthElement(price=str(i[0]), amount=str(i[1])))
            asks = []
            for i in order_book["asks"]:
                asks.append(service.DepthElement(price=str(i[0]), amount=str(i[1])))
            try:
                timestamp = order_book["last_update"]
            except:
                timestamp = 0
            return service.Depth(bids=bids, asks=asks, timestamp=timestamp, error="")

    def ping(self, request, context):
        return service.Pong(time=int(time.time() * 1000))


def serve():
    depth_handler = exchange.get_websockets_handler(orderbook=order_book, lock=lock)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=definitions.MAX_GRPC_WORKERS))
    rpc.add_AdapterServicer_to_server(Server(exchange), server)
    server.add_insecure_port('{0}:{1}'.format(config.LISTEN_HOST, config.LISTEN_PORT))
    server.start()
    depth_handler.start()
    depth_timestamp_checker()


if __name__ == "__main__":
    serve()
