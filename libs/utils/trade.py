from libs.utils.order import Order


class Trade(Order):
    def __init__(self, order_id, time, ticker, status, side, fee_amount, fee_currency, order_price, order_total,
                 token_amount):
        super().__init__(order_id, time, ticker, status, side)
        self.fee_amount = fee_amount
        self.fee_currency = fee_currency
        self.order_price = order_price
        self.order_total = order_total
        self.token_amount = token_amount
