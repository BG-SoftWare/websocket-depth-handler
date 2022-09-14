import grpc
import proto.adapter_pb2_grpc as rpc
import proto.adapter_pb2 as service_entities
from libs.utils.order import Order
from libs.utils.balance import Balance
from libs.utils.trade import Trade
from libs.utils.order_book import OrderBook
from decimal import Decimal

class GRPCClient(object):
    def __init__(self, address):
        channel = grpc.insecure_channel(address)
        self.connection = rpc.AdapterStub(channel)

    def get_depth(self):
        data = self.connection.get_depth(service_entities.Empty)
        symbol = ""
        bids = []
        asks = []
        timestamp = -1
        if data.error == "":
            for i in data.bids:
                bids.append([Decimal(i.price), Decimal(i.amount)])
            for i in data.asks:
                asks.append([Decimal(i.price), Decimal(i.amount)])
            timestamp = data.timestamp
            return OrderBook(symbol,bids,asks,timestamp)
        raise ConnectionError(data.error)

    def place_order(self, route, token_amount, token_price):
        data = self.connection.place_order(
            service_entities.RequestCreateOrder(route=route, token_amount=token_amount, token_price=token_price))
        if data.error == "":
            return Order(id=data.id, time=data.time, ticker=data.ticker, status=data.status, route=data.route)
        else:
            raise ConnectionError(data.error)

    def cancel_order(self, order):
        service_entity_order = service_entities.Order(**dict(order))
        data = self.connection.cancel_order(service_entity_order)
        if data.error == "":
            return True
        else:
            raise ConnectionError(data.error)

    def get_balances(self):
        balances = {}
        data = self.connection.cancel_order(service_entities.Empty)
        if data.error == "":
            for balance in data.balances:
                balances[balance.asset] = Balance(balance.asset, Decimal(balance.free), Decimal(balance.locked))
            return balances
        else:
            raise ConnectionError(data.error)

    def get_trade_info(self, order):
        service_entity_order = service_entities.Order(**dict(order))
        data = self.connection.get_trade_info(service_entities.RequestTradeInfo(order=service_entity_order))
        if data.error == "":
            return Trade(data.id, data.time, data.ticker, data.status, data.route, Decimal(data.fee_amount), data.fee_currency,
                         Decimal(data.order_price), Decimal(data.order_total), Decimal(data.token_amount))
        else:
            raise ConnectionError(data.error)

    def get_order_status(self, order):
        service_entity_order = service_entities.Order(**dict(order))
        data = self.connection.get_trade_info(service_entities.RequestTradeInfo(order=service_entity_order))
        if data.error == "":
            return Order(data.id, data.time, data.ticker, data.status, data.route)
        else:
            raise ConnectionError(data.error)

    def buy_fee_token_on_market_for_usdt(self, amount_usdt):
        data = self.connection.buy_fee_token_on_market_for_usdt(
            service_entities.BuyFeeTokenRequest(usdt_amount=str(amount_usdt)))
        if data.error == "":
            return Decimal(data.token_amount), Decimal(data.token_price)
        else:
            raise ConnectionError(data.error)
