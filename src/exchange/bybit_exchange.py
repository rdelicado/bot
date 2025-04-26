from pybit.unified_trading import HTTP
from dotenv import load_dotenv
import os

load_dotenv()

def get_bybit_session():
    session = HTTP(
        testnet=False,  # No testnet
        api_key=os.getenv("BYBIT_API_KEY"),
        api_secret=os.getenv("BYBIT_API_SECRET"),
    )
    session.endpoint = "https://api-demo.bybit.com"
    return session