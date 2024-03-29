import threading

import websocket


class Client(threading.Thread):
    def __init__(self, url, exchange_name):
        super().__init__()
        # create websocket connection
        self.ws = websocket.WebSocketApp(
            url=url,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close,
            on_open=self.on_open
        )
        self.exchange_name = exchange_name

    # keep connection alive
    def run(self):
        while True:
            self.ws.run_forever()

    # convert message to dict, process update
    def on_message(self, message):
        print(message)
        pass

    # catch errors
    def on_error(self, error):
        print(error)

    # run when websocket is closed
    def on_close(self):
        print("### closed ###")

    # run when websocket is initialised
    def on_open(self):
        print(f'Connected to {self.exchange_name}\n')
