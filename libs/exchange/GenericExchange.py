import proto.adapter_pb2 as service_entities


class GenericExhange(object):
    required_args = []
    ws_controller = None
    options = {
        "is_websockets": False,
        "is_buy_fee_token": False
    }

    def __init__(self, args):
        pass

    def get_websockets_handler(self, orderbook, lock):
        if self.ws_controller is None and self.options["is_websockets"]:
            raise NotImplementedError("You must override ws_controller")
        return self.ws_controller

    def _get_required_args(self):
        if len(self.required_args) == 0:
            raise NotImplementedError("You must enter required args to required_args array")
        return self.required_args

    def place_order(self, route, token_amount, token_price):
        raise NotImplementedError("You must implement place_order")

    def cancel_order(self, order):
        raise NotImplementedError("You must implement cancel_order")

    def get_order_status(self, order):
        raise NotImplementedError("You must implement get_order_status")

    def get_balances(self):
        raise NotImplementedError("You must implement get_balances")

    def get_trade_info(self, order):
        raise NotImplementedError("You must implement get_trade_info")

    def buy_fee_token_on_market_for_usdt(self, amount_usdt):
        if self.options["is_buy_fee_token"]:
            raise NotImplementedError("You must implement buy_fee_token_on_market_for_usdt")
        else:
            return service_entities.BuyFeeTokenRequest(token_amount="", token_price="",
                                                       error="This exchange dont have this feature")

    def place_market_order(self, route, token_amount):
        raise NotImplementedError("You must implement place_market_order")
