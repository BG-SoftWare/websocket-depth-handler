import logging
from libs.exchange.GenericExchange import GenericExhange
import requests
import uuid
import time
from urllib.parse import urlencode
import hmac
import hashlib
import proto.adapter_pb2 as service_entities
from decimal import Decimal
from libs.exchange.ws.binance import Binance as Binance_ws
import traceback
import definitions

class Binance(GenericExhange):
    required_args = ["api_key", "api_sec", "ticker", "recv_window"]
    ws_controller = Binance_ws
    options = {
        "is_websockets": True,
        "is_buy_fee_token": True
    }

    __api_key = None
    __api_sec = None
    __ticker = None
    __ws_url = None
    __api_url = None
    __bridge_url = None
    __price_precision = None
    __recv_window = None
    currencies = ["BNB"]

    def __init__(self, args):
        if list(args.keys()).sort() == self._get_required_args().sort():
            self.__api_key = args["api_key"]
            self.__api_sec = args["api_sec"]
            self.__ticker = args["ticker"]
            self.__recv_window = args["recv_window"]
            self.__ws_url = "wss://stream.binance.com:9443/ws/{0}@depth@100ms".format(self.__ticker.lower())
        super().__init__(args)


    def get_websockets_handler(self, orderbook, lock):
        return self.ws_controller(url=self.__ws_url, exchange="Binance", orderbook=orderbook,
                                  ticker=self.__ticker, lock=lock)
