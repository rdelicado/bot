from exchange.bybit_client import BybitClient

def test_get_balance():
    client = BybitClient()
    balance = client.get_balance()
    assert balance is not None
    assert float(balance) >= 0

def test_get_price():
    client = BybitClient()
    price = client.get_price("BTCUSDT")
    assert price is not None
    assert float(price) > 0
