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
