from decimal import Decimal


class OrderBook(object):
    def __init__(self, symbol, bids, asks, timestamp):
        self.bids = bids
        self.asks = asks
        self.symbol = symbol
        self.timestamp = timestamp

    """def calculate(self, route, amount):
        sell_price, avg_sell_price, got_amount = 0, 0, 0
        counter = 0
        sell_amount = amount
        if route == "SELL":
            bids_r = self.bids
        elif route == "BUY":
            bids_r = self.asks
        else:
            return
        for i in bids_r:
            price, amount_stack = Decimal(i[0]), Decimal(i[1])
            if amount_stack >= amount:
                got_amount = price * amount
                return price, price, got_amount
            else:
                if sell_amount > amount_stack:
                    got_amount += price * amount_stack
                    avg_sell_price += price
                    counter += 1
                    sell_amount -= amount_stack

                else:
                    avg_sell_price += price
                    counter += 1
                    got_amount += price * sell_amount
                    return price, avg_sell_price / counter, got_amount"""

    """#route направление продажи
    #amount количество сол для покупки/продажи
    def calculate(self, route, amount):
        if route == "BUY":
            buy_price, avg_buy_price, usdt_amount, is_first = 0,0,0,True
            for i in self.asks:
                if Decimal(i[1]) >= amount and is_first:
                    return Decimal(i[0]), Decimal(i[0]), amount * Decimal(i[0])
                elif Decimal(i[1]) < amount:
                    is_first = False
                    usdt_amount += Decimal(i[1]) * Decimal(i[0])
                    amount -= Decimal(i[1])
                    continue
                if is_first == False:
                    if Decimal(i[1]) <= amount:
                        usdt_amount += Decimal(i[1]) * Decimal(i[0])
                        amount -= Decimal(i[1])
                        if amount == 0:
                            return Decimal(i[0]), usdt_amount / Decimal(i[0]), usdt_amount
                    else:
                        usdt_amount += amount * Decimal(i[0])
                        return Decimal(i[0]), usdt_amount / Decimal(i[0]), usdt_amount

        elif route == "SELL":
            sell_price, avg_sell_price, usdt_amount, is_first = 0,0,0,True
            for i in self.bids:
                if Decimal(i[1]) >= amount:
                    return Decimal(i[0]), Decimal(i[0]), amount * Decimal(i[0])
                elif Decimal(i[1]) < amount:
                    is_first = False
                    usdt_amount += Decimal(i[1]) * Decimal(i[0])
                    amount -= Decimal(i[1])
                    continue
                if is_first == False:
                    if Decimal(i[1]) <= amount:
                        usdt_amount += Decimal(i[1]) * Decimal(i[0])
                        amount -= Decimal(i[1])
                        if amount == 0:
                            return Decimal(i[0]), usdt_amount / Decimal(i[0]), usdt_amount
                    else:
                        usdt_amount += amount * Decimal(i[0])
                        return Decimal(i[0]), usdt_amount / Decimal(i[0]), usdt_amount"""

    #route направление продажи
    #amount количество сол для покупки/продажи
    def calculate(self, route, amount=0):
        amount_orig = amount
        if route == "BUY":
            if amount > 0:
                buy_price, avg_buy_price, usdt_amount, is_first = 0,0,0,True
                for i in self.asks:
                    if Decimal(i[1]) >= amount and is_first:
                        return Decimal(i[0]), Decimal(i[0]), amount * Decimal(i[0])
                    elif Decimal(i[1]) < amount and is_first:
                        is_first = False
                        usdt_amount += Decimal(i[1]) * Decimal(i[0])
                        amount -= Decimal(i[1])
                        continue
                    if is_first == False:
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
                sell_price, avg_sell_price, usdt_amount, is_first = 0,0,0,True
                for i in self.bids:
                    if Decimal(i[1]) >= amount and is_first:
                        return Decimal(i[0]), Decimal(i[0]), amount * Decimal(i[0])
                    elif Decimal(i[1]) < amount and is_first:
                        is_first = False
                        usdt_amount += Decimal(i[1]) * Decimal(i[0])
                        amount -= Decimal(i[1])
                        continue
                    if is_first == False:
                        if Decimal(i[1]) <= amount:
                            usdt_amount += Decimal(i[1]) * Decimal(i[0])
                            amount -= Decimal(i[1])
                            if amount == 0:
                                return Decimal(i[0]), usdt_amount / amount_orig, usdt_amount
                        else:
                            usdt_amount += amount * Decimal(i[0])
                            return Decimal(i[0]), usdt_amount / amount_orig, usdt_amount


    def getbid(self):
        return self.bids[0]

    def getask(self):
        return self.asks[0]

    def order_fork(self, price, route, step):
        if route == "SELL":
            for i in range(len(self.bids)):
                if Decimal(self.bids[i][0]) == price:
                    return price, Decimal(self.bids[i+step][0])
        elif route == "BUY":
            for i in range(len(self.asks)):
                if Decimal(self.asks[i][0]) == price:
                    return price, Decimal(self.asks[i + step][0])

    def order_stop_limit(self, price, route, step):
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
