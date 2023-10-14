from decimal import Decimal


class OrderBook(object):
    def __init__(self, symbol: str, bids: list, asks: list):
        self.bids = bids
        self.asks = asks
        self.symbol = symbol

    def calculate(self, route: str, amount: Decimal = 0):
        """
        params: route - trade side (BUY or SELL)
        params: amount - amount to trade
        """
        amount_orig = amount
        if route == "BUY":
            if amount > 0:
                buy_price, avg_buy_price, usdt_amount, is_first = 0, 0, 0, True
                for i in self.asks:
                    if Decimal(i[1]) >= amount and is_first:
                        return Decimal(i[0]), Decimal(i[0]), amount * Decimal(i[0])
                    elif Decimal(i[1]) < amount and is_first:
                        is_first = False
                        usdt_amount += Decimal(i[1]) * Decimal(i[0])
                        amount -= Decimal(i[1])
                        continue
                    if not is_first:
                        if Decimal(i[1]) <= amount:
                            usdt_amount += Decimal(i[1]) * Decimal(i[0])
                            amount -= Decimal(i[1])
                            if amount == 0:
                                return Decimal(i[0]), usdt_amount / amount_orig, usdt_amount
                        else:
                            usdt_amount += amount * Decimal(i[0])
                            return Decimal(i[0]), usdt_amount / amount_orig, usdt_amount
        elif route == "SELL":
            if amount > 0:
                sell_price, avg_sell_price, usdt_amount, is_first = 0, 0, 0, True
                for i in self.bids:
                    if Decimal(i[1]) >= amount and is_first:
                        return Decimal(i[0]), Decimal(i[0]), amount * Decimal(i[0])
                    elif Decimal(i[1]) < amount and is_first:
                        is_first = False
                        usdt_amount += Decimal(i[1]) * Decimal(i[0])
                        amount -= Decimal(i[1])
                        continue
                    if not is_first:
                        if Decimal(i[1]) <= amount:
                            usdt_amount += Decimal(i[1]) * Decimal(i[0])
                            amount -= Decimal(i[1])
                            if amount == 0:
                                return Decimal(i[0]), usdt_amount / amount_orig, usdt_amount
                        else:
                            usdt_amount += amount * Decimal(i[0])
                            return Decimal(i[0]), usdt_amount / amount_orig, usdt_amount

    def get_best_bid(self):
        return self.bids[0]

    def get_best_ask(self):
        return self.asks[0]

    def order_fork(self, price: Decimal, route: str, step: int):
        if route == "SELL":
            for i in range(len(self.bids)):
                if Decimal(self.bids[i][0]) == price:
                    return price, Decimal(self.bids[i + step][0])
        elif route == "BUY":
            for i in range(len(self.asks)):
                if Decimal(self.asks[i][0]) == price:
                    return price, Decimal(self.asks[i + step][0])

    def order_stop_limit(self, price: Decimal, route: str, step: int):
        if route == "SELL":
            for i in range(len(self.bids)):
                if Decimal(self.bids[i][0]) == price:
                    if i + step >= len(self.bids) - 1:
                        return Decimal(self.bids[-1][0]), Decimal(self.bids[-1][0])
                    return Decimal(self.bids[i + step][0]), Decimal(self.bids[i + step][0])
        elif route == "BUY":
            for i in range(len(self.asks)):
                if Decimal(self.asks[i][0]) == price:
                    if i + step >= len(self.asks) - 1:
                        return Decimal(self.asks[-1][0]), Decimal(self.asks[-1][0])
                    return Decimal(self.asks[i + step][0]), Decimal(self.asks[i + step][0])
