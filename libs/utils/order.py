class Order(object):
    def __init__(self,id, time, ticker, status, route):
        self.id = id
        self.time = time
        self.ticker = ticker
        self.status = status
        self.route = route
