from pybit.unified_trading import HTTP
import os
from dotenv import load_dotenv

load_dotenv()

session = HTTP(
    testnet=False,  # No testnet
    api_key=os.getenv("BYBIT_API_KEY"),
    api_secret=os.getenv("BYBIT_API_SECRET"),
)
# Forzar endpoint demo trading
session.endpoint = "https://api-demo.bybit.com"

def ver_saldo():
    try:
        balance = session.get_wallet_balance(accountType="UNIFIED")
        coins = balance['result']['list'][0]['coin']
        for coin in coins:
            print(f"Moneda: {coin['coin']}")
            print(f"  Saldo disponible: {coin['walletBalance']}")
            print(f"  Saldo total (equity): {coin['equity']}")
            print("-" * 30)
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    ver_saldo()