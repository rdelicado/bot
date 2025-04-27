import numpy as np 

def calcular_ema(cierres, periodo):
    """
    Calcula la EMA (Exponential Moving Average) para una lista de precios de cierre.
    Devuelve una lista con la EMA para cada punto a partir de 'periodo'-1.
    """
    if len(cierres) < periodo:
        return []

    ema = []
    k = 2 / (periodo + 1)
    # EMA inicial: la media simple de los primeros 'periodo' cierres
    ema_actual = sum(cierres[:periodo]) / periodo
    ema.append(ema_actual)
    # Calcula la EMA para el resto de los datos
    for precio in cierres[periodo:]:
        ema_actual = precio * k + ema_actual * (1 - k)
        ema.append(ema_actual)
    return ema

def calcular_adx(cierres, altos, bajos, periodo=14):
    """
    Calcula el ADX (Average Directional Index).
    Devuelve una lista con el ADX para cada punto a partir de 'periodo'.
    """
    if len(cierres) < periodo + 1:
        return []

    tr_list = []
    plus_dm = []
    minus_dm = []

    for i in range(1, len(cierres)):
        tr = max(
            altos[i] - bajos[i],
            abs(altos[i] - cierres[i - 1]),
            abs(bajos[i] - cierres[i - 1])
        )
        tr_list.append(tr)

        up_move = altos[i] - altos[i - 1]
        down_move = bajos[i - 1] - bajos[i]

        plus_dm.append(up_move if up_move > down_move and up_move > 0 else 0)
        minus_dm.append(down_move if down_move > up_move and down_move > 0 else 0)

    # Suavizado inicial
    tr14 = sum(tr_list[:periodo])
    plus_dm14 = sum(plus_dm[:periodo])
    minus_dm14 = sum(minus_dm[:periodo])

    adx_list = []
    for i in range(periodo, len(tr_list)):
        tr14 = tr14 - (tr14 / periodo) + tr_list[i]
        plus_dm14 = plus_dm14 - (plus_dm14 / periodo) + plus_dm[i]
        minus_dm14 = minus_dm14 - (minus_dm14 / periodo) + minus_dm[i]

        plus_di = 100 * (plus_dm14 / tr14) if tr14 != 0 else 0
        minus_di = 100 * (minus_dm14 / tr14) if tr14 != 0 else 0
        dx = 100 * abs(plus_di - minus_di) / (plus_di + minus_di) if (plus_di + minus_di) != 0 else 0

        if i == periodo:
            adx = dx
        else:
            adx = (adx_list[-1] * (periodo - 1) + dx) / periodo
        adx_list.append(adx)

    return adx_list

def calcular_rsi(cierres, periodo=14):
    if len(cierres) < periodo + 1:
        return []
    ganancias = []
    perdidas = []
    for i in range(1, periodo + 1):
        cambio = cierres[i] - cierres[i - 1]
        ganancias.append(max(cambio, 0))
        perdidas.append(abs(min(cambio, 0)))
    avg_ganancia = sum(ganancias) / periodo
    avg_perdida = sum(perdidas) / periodo
    rsi = []
    for i in range(periodo + 1, len(cierres)):
        cambio = cierres[i] - cierres[i - 1]
        ganancia = max(cambio, 0)
        perdida = abs(min(cambio, 0))
        avg_ganancia = (avg_ganancia * (periodo - 1) + ganancia) / periodo
        avg_perdida = (avg_perdida * (periodo - 1) + perdida) / periodo
        rs = avg_ganancia / avg_perdida if avg_perdida != 0 else 0
        rsi.append(100 - (100 / (1 + rs)) if avg_perdida != 0 else 100)
    return rsi

def calcular_macd(cierres, rapida=12, lenta=26, senal=9):
    if len(cierres) < lenta + senal:
        return [], [], []
    def ema(data, periodo):
        k = 2 / (periodo + 1)
        ema_actual = sum(data[:periodo]) / periodo
        resultado = [ema_actual]
        for precio in data[periodo:]:
            ema_actual = precio * k + ema_actual * (1 - k)
            resultado.append(ema_actual)
        return resultado
    ema_rapida = ema(cierres, rapida)
    ema_lenta = ema(cierres, lenta)
    macd_line = [r - l for r, l in zip(ema_rapida[-len(ema_lenta):], ema_lenta)]
    signal_line = ema(macd_line, senal)
    histograma = [m - s for m, s in zip(macd_line[-len(signal_line):], signal_line)]
    return macd_line, signal_line, histograma

def calcular_estocastico(cierres, altos, bajos, k_periodo=14, d_periodo=3):
    if len(cierres) < k_periodo:
        return [], []
    k_values = []
    for i in range(k_periodo - 1, len(cierres)):
        max_alto = max(altos[i - k_periodo + 1:i + 1])
        min_bajo = min(bajos[i - k_periodo + 1:i + 1])
        k = 100 * (cierres[i] - min_bajo) / (max_alto - min_bajo) if max_alto != min_bajo else 0
        k_values.append(k)
    d_values = []
    for i in range(d_periodo - 1, len(k_values)):
        d = sum(k_values[i - d_periodo + 1:i + 1]) / d_periodo
        d_values.append(d)
    return k_values, d_values

def calcular_squeeze_momentum(cierres, altos, bajos, bb_length=20, bb_mult=2.0, kc_length=20, kc_mult=1.5):
    if len(cierres) < max(bb_length, kc_length):
        return [], []

    # Bandas de Bollinger
    medias = [np.mean(cierres[i-bb_length+1:i+1]) for i in range(bb_length-1, len(cierres))]
    stds = [np.std(cierres[i-bb_length+1:i+1]) for i in range(bb_length-1, len(cierres))]
    bb_upper = [m + bb_mult*s for m, s in zip(medias, stds)]
    bb_lower = [m - bb_mult*s for m, s in zip(medias, stds)]

    # Canales de Keltner
    typical_prices = [(c + h + l)/3 for c, h, l in zip(cierres, altos, bajos)]
    ema_tp = []
    k = 2 / (kc_length + 1)
    ema_actual = np.mean(typical_prices[:kc_length])
    ema_tp.append(ema_actual)
    for precio in typical_prices[kc_length:]:
        ema_actual = precio * k + ema_actual * (1 - k)
        ema_tp.append(ema_actual)
    ema_tp = ema_tp[-(len(medias)):]  # Alinear longitudes

    tr = [max(altos[i] - bajos[i], abs(altos[i] - cierres[i-1]), abs(bajos[i] - cierres[i-1])) for i in range(1, len(cierres))]
    atr = []
    atr_actual = np.mean(tr[:kc_length-1])
    atr.append(atr_actual)
    for t in tr[kc_length-1:]:
        atr_actual = (atr_actual * (kc_length - 1) + t) / kc_length
        atr.append(atr_actual)
    atr = atr[-(len(medias)):]  # Alinear longitudes

    kc_upper = [m + kc_mult*a for m, a in zip(ema_tp, atr)]
    kc_lower = [m - kc_mult*a for m, a in zip(ema_tp, atr)]

    # Squeeze: True si banda de bollinger está dentro del canal de keltner
    squeeze_on = [(bb_upper[i] < kc_upper[i] and bb_lower[i] > kc_lower[i]) for i in range(len(medias))]

    # Momentum (diferencia entre cierre y media de cierre)
    momentum = [cierres[i+bb_length-1] - medias[i] for i in range(len(medias))]

    return momentum, squeeze_on

def calcular_volume_profile(cierres, volumenes, bins=20):
    """
    Calcula un perfil de volumen simple agrupando el volumen por rangos de precio (bins).
    Devuelve dos listas: los rangos de precio (centro de cada bin) y el volumen acumulado en cada bin.
    """
    if not cierres or not volumenes or len(cierres) != len(volumenes):
        return [], []
    min_precio = min(cierres)
    max_precio = max(cierres)
    rango = max_precio - min_precio
    if rango == 0:
        return [], []
    bin_size = rango / bins
    volumen_por_bin = [0] * bins
    bin_centers = [min_precio + (i + 0.5) * bin_size for i in range(bins)]
    for precio, vol in zip(cierres, volumenes):
        idx = int((precio - min_precio) / bin_size)
        if idx == bins:
            idx -= 1  # Incluir el valor máximo en el último bin
        volumen_por_bin[idx] += vol
    return bin_centers, volumen_por_bin