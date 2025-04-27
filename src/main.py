from exchange.bybit_client import BybitClient
from indicators.technical_indicators import (
    calcular_ema,
    calcular_adx,
    calcular_rsi,
    calcular_macd,
    calcular_estocastico,
    calcular_squeeze_momentum,
    calcular_volume_profile
)

if __name__ == "__main__":
    client = BybitClient()
    client.get_saldo()
    print("Balance UDST: ", client.get_balance())
    print("Precio BTC/USDT:", client.get_price("BTCUSDT"))

    # 1. Obtener precios OHLC
    cierres, altos, bajos = client.get_candles("BTCUSDT", interval="240", limit=1000, category="linear")
    print(f"Último cierre: {cierres[-1] if cierres else 'No hay datos disponibles'}")
    print(f"Total cierres descargados: {len(cierres)}")

    # 2. Calcular EMA(10), EMA(55), EMA(200)
    ema_10 = calcular_ema(cierres, 10)
    ema_55 = calcular_ema(cierres, 55)
    ema_200 = calcular_ema(cierres, 200)
    print(f"Última EMA 10: {ema_10[-1] if ema_10 else 'No hay suficientes datos'}")
    print(f"Última EMA 55: {ema_55[-1] if ema_55 else 'No hay suficientes datos'}")
    print(f"Última EMA 200: {ema_200[-1] if ema_200 else 'No hay suficientes datos'}")

    # 3. Calcular ADX
    adx_14 = calcular_adx(cierres, altos, bajos, periodo=14)
    print(f"Último ADX 14: {adx_14[-1] if adx_14 else 'No hay suficientes datos'}")

    # 4. Calcular RSI
    rsi_14 = calcular_rsi(cierres, periodo=14)
    print(f"Último RSI 14: {rsi_14[-1] if rsi_14 else 'No hay suficientes datos'}")

    # 5. Calcular MACD
    macd_line, signal_line, histograma = calcular_macd(cierres)
    print(f"Último MACD: {macd_line[-1] if macd_line else 'No hay suficientes datos'}")
    print(f"Última Señal MACD: {signal_line[-1] if signal_line else 'No hay suficientes datos'}")
    print(f"Último Histograma MACD: {histograma[-1] if histograma else 'No hay suficientes datos'}")

    # 6. Calcular Estocástico
    k_values, d_values = calcular_estocastico(cierres, altos, bajos)
    print(f"Último %K Estocástico: {k_values[-1] if k_values else 'No hay suficientes datos'}")
    print(f"Último %D Estocástico: {d_values[-1] if d_values else 'No hay suficientes datos'}")

    # 7. Calcular Squeeze Momentum Indicator
    momentum, squeeze_on = calcular_squeeze_momentum(cierres, altos, bajos)
    if momentum and squeeze_on:
        print(f"Último Momentum Squeeze: {momentum[-1]}")
        print(f"Squeeze activo: {'Sí' if squeeze_on[-1] else 'No'}")
    else:
        print("No hay suficientes datos para Squeeze Momentum Indicator.")

    # 8. Calcular Volume Profile
    volumenes = client.get_volumenes("BTCUSDT", interval="240", limit=1000, category="linear")
    bin_centers, volumen_por_bin = calcular_volume_profile(cierres, volumenes)
    if bin_centers and volumen_por_bin:
        print("Perfil de Volumen (precio, volumen):")
        for precio, vol in zip(bin_centers, volumen_por_bin):
            print(f"{precio:.2f}: {vol}")
    else:
        print("No hay suficientes datos para Volume Profile.")

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
