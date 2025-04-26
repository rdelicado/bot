from pybit.unified_trading import HTTP
import os
from dotenv import load_dotenv
import json

load_dotenv()


session = HTTP(
    testnet=True,
    api_key=os.getenv("BYBIT_API_KEY"),
    api_secret=os.getenv("BYBIT_API_SECRET"),
)

def ver_saldo():
    try:
        balance = session.get_wallet_balance(accountType="UNIFIED")
        print(json.dumps(balance, indent=2))
        """ coins = balance['result']['list'][0]['coin']
        for coin in coins:
            if coin['coin'] == 'USDT':
                print(f"Saldo disponible USDT: {coin['walletBalance']}")
                print(f"Saldo total USDT (equity): {coin['equity']}") """
    except Exception as e:
        print(f"❌ Error: {str(e)}")

if __name__ == "__main__":
    ver_saldo()

