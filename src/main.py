from exchange.bybit_client import BybitClient

if __name__ == "__main__":
    client = BybitClient()
    client.get_saldo()
    print("Balance UDST: ", client.get_balance())
    print("Precio BTC/USDT:", client.get_price("BTCUSDT"))