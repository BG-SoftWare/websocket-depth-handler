def prepare_csv_file(filename):
    open(filename, "a").write(
        "\"DateTime\"; \"action\";\"delta\"; \"price_buy\"; \"avg_price_buy\"; \"usdt_buy_amount\"; "
        "\"price_sell\"; \"avg_price_sell\"; \"usdt_sell_amount\"; \"profit\"; binance_coin_1;binance_coin_2;coinsbit_coin_1;coinsbit_coin_2" + "\n")
    pass


def print_to_csv(filename, data):
    open(filename, "a").write(";".join(data).replace(".", ",") + "\n")