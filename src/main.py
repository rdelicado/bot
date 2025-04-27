from exchange.bybit_client import BybitClient
from indicators.technical_indicators import calcular_ema, calcular_adx

if __name__ == "__main__":
    client = BybitClient()
    client.get_saldo()
    print("Balance UDST: ", client.get_balance())
    print("Precio BTC/USDT:", client.get_price("BTCUSDT"))

    # 1. Obtener precios OHLC
    cierres, altos, bajos = client.get_candles("BTCUSDT", interval="240", limit=1000, category="linear")
    print(f"Último cierre: {cierres[-1] if cierres else 'No hay datos disponibles'}")
    print(f"Total cierres descargados: {len(cierres)}")

    # 2. Calcular EMA(10) y EMA(55)
    ema_10 = calcular_ema(cierres, 10)
    ema_55 = calcular_ema(cierres, 55)
    print(f"Última EMA 10: {ema_10[-1] if ema_10 else 'No hay suficientes datos'}")
    print(f"Última EMA 55: {ema_55[-1] if ema_55 else 'No hay suficientes datos'}")

    # 3. Calcular ADX
    adx_14 = calcular_adx(cierres, altos, bajos, periodo=14)
    print(f"Último ADX 14: {adx_14[-1] if adx_14 else 'No hay suficientes datos'}")


''''
| Intervalo API | Descripción      |
|:-------------:|:----------------|
| "1"           | 1 minuto        |
| "3"           | 3 minutos       |
| "5"           | 5 minutos       |
| "15"          | 15 minutos      |
| "30"          | 30 minutos      |
| "60"          | 1 hora          |
| "120"         | 2 horas         |
| "240"         | 4 horas         |
| "360"         | 6 horas         |
| "720"         | 12 horas        |
| "D"           | 1 día           |
| "W"           | 1 semana        |
| "M"           | 1 mes (aprox)   |
'''
