from libs.exchange.ws.client import Client
from json import loads
from datetime import datetime
from decimal import Decimal
import time
import requests


class Binance(Client):
    def __init__(self, url, exchange, orderbook, ticker, lock):
        super().__init__(url, exchange)
        # local data management
        self.orderbook = orderbook
        self.lock = lock
        self.updates = 0
        self.last_update = orderbook
        self.ticker = ticker

    # convert message to dict, process update
    def on_message(self, message):
        data = loads(message)
        # check for orderbook, if empty retrieve
        if len(self.orderbook) == 0:
            for key, value in self.get_snapshot().items():
                self.orderbook[key] = value

        # get lastUpdateId
        lastUpdateId = self.orderbook['lastUpdateId']

        # drop any updates older than the snapshot
        if self.updates == 0:
            if data['U'] <= lastUpdateId + 1 and data['u'] >= lastUpdateId + 1:
                self.orderbook['lastUpdateId'] = data['u']
                self.process_updates(data)

        # check if update still in sync with orderbook
        elif data['U'] == lastUpdateId + 1:
            self.orderbook['lastUpdateId'] = data['u']
            self.process_updates(data)
        else:
            print('Out of sync, abort')

    # Loop through all bid and ask updates, call manage_orderbook accordingly
    def process_updates(self, data):
        with self.lock:
            for update in data['b']:
                # print(update)
                fix = [Decimal(update[0]), Decimal(update[1])]
                self.manage_orderbook('bids', fix)
            for update in data['a']:
                # print(update)
                fix = [Decimal(update[0]), Decimal(update[1])]
                self.manage_orderbook('asks', fix)
            self.last_update['last_update'] = int(time.time() * 1000)

    # Update orderbook, differentiate between remove, update and new
    def manage_orderbook(self, side, update):
        # extract values
        price, qty = update

        # loop through orderbook side
        for x in range(0, len(self.orderbook[side])):
            if price == self.orderbook[side][x][0]:
                # when qty is 0 remove from orderbook, else
                # update values
                if qty == 0:
                    del self.orderbook[side][x]
                    break
                else:
                    self.orderbook[side][x] = update
                    break
            # if the price level is not in the orderbook,
            # insert price level, filter for qty 0
            elif ((price > self.orderbook[side][x][0] and side == 'bids') or
                  (price < self.orderbook[side][x][0] and side == 'asks')):
                if qty != 0:
                    self.orderbook[side].insert(x, update)
                    break
                else:
                    break

    # retrieve orderbook snapshot
    def get_snapshot(self):
        r = requests.get('https://www.binance.com/api/v1/depth?symbol=' + self.ticker + '&limit=1000')
        data = loads(r.content.decode())
        data["bids"] = [[Decimal(x[0]), Decimal(x[1])] for x in data["bids"]]
        data["asks"] = [[Decimal(x[0]), Decimal(x[1])] for x in data["asks"]]
        return data

    def on_close(self):
        with self.lock:
            self.orderbook.clear()
        super().on_close()

    def on_error(self, error):
        with self.lock:
            self.orderbook.clear()
        super().on_close()

    def on_open(self):
        with self.lock:
            self.orderbook.clear()
        super().on_open()