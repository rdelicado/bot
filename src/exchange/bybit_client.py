''''
Aquí pondrás la lógica de negocio específica para tu bot:

Métodos para obtener balance, precios, colocar órdenes, etc., usando la conexión de bybit_exchange.py.
Así, si cambias de exchange, solo cambias el client y no todo el código.
Ejemplo: métodos como get_balance(), get_price(symbol), place_order(...), etc.
'''
from .bybit_exchange import get_bybit_session

class BybitClient:
    def __init__(self):
        self.session = get_bybit_session()

    def get_saldo(self):
        try:
            saldo = self.session.get_wallet_balance(accountType="UNIFIED")
            coins = saldo['result']['list'][0]['coin']
            for coin in coins:
                print(f"Moneda: {coin['coin']}")
                print(f"  Saldo disponible: {coin['walletBalance']}")
                print(f"  Saldo total (equity): {coin['equity']}")
                print("-" * 30)
        except Exception as e:
            print(f"❌ Error al obtener el saldo: {e}")
            return None
    
    def get_balance(self):
        try:
            balance = self.session.get_wallet_balance(accountType="UNIFIED")
            coins = balance['result']['list'][0]['coin']
            for coin in coins:
                if coin['coin'] == 'USDT':
                    return coin['walletBalance']
            return 0
        except Exception as e:
            print(f"❌ Error al obtener el balance: {e}")
            return None

    def get_price(self, symbol):
        try:
            ticker = self.session.get_tickers(category="linear", symbol=symbol)
            return ticker['result']['list'][0]['lastPrice']
        except Exception as e:
            print(f"❌ Error al obtener el price: {e}")
            return None
