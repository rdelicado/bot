from .bybit_exchange import get_bybit_session

def abrir_posicion(symbol, qty, side, tipo_orden="Market"):
    """
    Abre una posición en Bybit.
    side: "Buy" o "Sell"
    tipo_orden: "Market" o "Limit"
    """
    session = get_bybit_session()
    orden = session.place_order(
        category="linear",
        symbol=symbol,
        side=side,
        order_type=tipo_orden,
        qty=qty,
        time_in_force="GoodTillCancel"
    )
    return orden

def cerrar_posicion(symbol, qty, side, tipo_orden="Market"):
    """
    Cierra una posición en Bybit.
    side: "Buy" o "Sell" (opuesto a la posición abierta)
    """
    session = get_bybit_session()
    orden = session.place_order(
        category="linear",
        symbol=symbol,
        side=side,
        order_type=tipo_orden,
        qty=qty,
        reduce_only=True,
        time_in_force="GoodTillCancel"
    )
    return orden