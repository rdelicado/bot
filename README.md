# 🤖 Crypto Trading Bot

[![Language](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Exchange](https://img.shields.io/badge/Exchange-Bybit-orange.svg)](https://www.bybit.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![API](https://img.shields.io/badge/API-CCXT-red.svg)](https://github.com/ccxt/ccxt)
[![Framework](https://img.shields.io/badge/Framework-Pandas-purple.svg)](https://pandas.pydata.org/)
[![Trading](https://img.shields.io/badge/Trading-Algorithmic-gold.svg)](https://www.investopedia.com/articles/active-trading/101014/basics-algorithmic-trading-concepts-and-examples.asp)

## 📋 Descripción

**Crypto Trading Bot** es un sistema de trading algorítmico avanzado diseñado para operar automaticamente en el mercado de criptomonedas utilizando la plataforma Bybit. El bot implementa múltiples indicadores técnicos, gestión de riesgo y estrategias de trading automatizadas para maximizar las oportunidades de mercado.

El sistema está construido con Python y utiliza bibliotecas especializadas como CCXT para conectividad con exchanges, TA-Lib para análisis técnico, y PyBit para interacción específica con la API de Bybit. Incluye capacidades de backtesting, análisis de volumen, y implementación de estrategias personalizadas.

### Objetivos del Proyecto

- **Trading Automatizado**: Ejecución automática de operaciones basadas en señales técnicas
- **Análisis Técnico**: Implementación de indicadores técnicos profesionales
- **Gestión de Riesgo**: Sistemas avanzados de control de pérdidas y ganancias
- **Multi-timeframe**: Análisis en múltiples marcos temporales
- **Backtesting**: Pruebas históricas de estrategias
- **Real-time Data**: Procesamiento de datos de mercado en tiempo real

## 🏗️ Arquitectura del Sistema

```
                    ┌─────────────────────────────────────┐
                    │         Trading Engine             │
                    │       (main.py)                    │
                    └─────────────────┬───────────────────┘
                                      │
            ┌─────────────────────────┼─────────────────────────┐
            │                         │                         │
    ┌───────▼────────┐    ┌──────────▼──────────┐    ┌───────▼────────┐
    │   Exchange      │    │    Technical        │    │   Strategy     │
    │   Connector     │    │    Indicators       │    │   Engine       │
    │   (Bybit API)   │    │   (TA Library)      │    │  (Strategies)  │
    └─────────────────┘    └─────────────────────┘    └────────────────┘
            │                         │                         │
    ┌───────▼────────┐    ┌──────────▼──────────┐    ┌───────▼────────┐
    │   Real-time     │    │    Signal           │    │   Risk         │
    │   Market Data   │    │    Generation       │    │   Management   │
    │   (OHLCV)       │    │   (Buy/Sell)        │    │   (Position)   │
    └─────────────────┘    └─────────────────────┘    └────────────────┘

                    ┌─────────────────────────────────────┐
                    │         Data Pipeline              │
                    ├─────────────────┬───────────────────┤
                    │    Market       │     Analysis      │
                    │    Data         │     & Signals     │
                    │  (Candles)      │   (Indicators)    │
                    └─────────────────┴───────────────────┘

                    ┌─────────────────────────────────────┐
                    │        Risk Management             │
                    │                                     │
                    │ Stop Loss │ Take Profit │ Position │
                    │   Orders  │   Targets   │   Size   │
                    │           │             │ Control  │
                    └─────────────────────────────────────┘
```

## 🚀 Características Principales

### 📊 Indicadores Técnicos
- **EMA (Exponential Moving Average)**: Medias móviles exponenciales (10, 55, 200)
- **RSI (Relative Strength Index)**: Oscilador de momento para identificar sobrecompra/sobreventa
- **MACD (Moving Average Convergence Divergence)**: Indicador de momentum y tendencia
- **ADX (Average Directional Index)**: Medidor de fuerza de tendencia
- **Stochastic Oscillator**: Indicador de momentum para puntos de entrada/salida
- **Squeeze Momentum**: Identificador de períodos de baja volatilidad
- **Volume Profile**: Análisis de distribución de volumen por precio

### 🔄 Conectividad de Exchange
- **Bybit API Integration**: Conexión nativa con la API de Bybit
- **Real-time Data**: Obtención de datos OHLCV en tiempo real
- **Multiple Timeframes**: Soporte para múltiples marcos temporales (1m a 1M)
- **Account Management**: Gestión de balance y posiciones
- **Order Execution**: Ejecución automática de órdenes de compra/venta
- **Demo Trading**: Modo de prueba sin riesgo financiero

### 📈 Estrategias de Trading
- **TradingLatino Strategy**: Estrategia personalizada basada en múltiples indicadores
- **Trend Following**: Estrategias de seguimiento de tendencia
- **Mean Reversion**: Estrategias de reversión a la media
- **Breakout Detection**: Detección de rupturas de niveles importantes
- **Multi-timeframe Analysis**: Análisis en múltiples marcos temporales
- **Custom Strategies**: Framework para implementar estrategias personalizadas

### 🛡️ Gestión de Riesgo
- **Position Sizing**: Cálculo automático del tamaño de posición
- **Stop Loss Management**: Gestión automática de stop loss
- **Take Profit Targets**: Objetivos de ganancia automatizados
- **Risk-Reward Ratio**: Control de relación riesgo-beneficio
- **Maximum Drawdown**: Control de pérdida máxima
- **Portfolio Risk**: Gestión de riesgo a nivel de cartera

### 🔧 Herramientas de Desarrollo
- **Jupyter Notebooks**: Entorno de desarrollo y análisis
- **Backtesting Framework**: Sistema de pruebas históricas
- **Configuration Management**: Gestión de configuración con YAML
- **Logging System**: Sistema de registro de actividades
- **Unit Testing**: Suite de pruebas unitarias con pytest
- **Data Analysis**: Herramientas de análisis con pandas y numpy

### 📱 Monitoreo y Alertas
- **Real-time Monitoring**: Monitoreo en tiempo real de posiciones
- **Performance Metrics**: Métricas de rendimiento detalladas
- **Trade History**: Historial completo de operaciones
- **Alert System**: Sistema de alertas para eventos importantes
- **Dashboard Integration**: Integración con dashboards de monitoreo
- **Risk Alerts**: Alertas de gestión de riesgo

## 🛠️ Instalación y Configuración

### Requisitos Previos

```bash
# Python 3.8 o superior
python --version

# pip para gestión de paquetes
pip --version

# Git para control de versiones
git --version
```

### Instalación del Proyecto

```bash
# Clonar el repositorio
git clone https://github.com/rdelicado/bot.git
cd bot

# Crear entorno virtual
python -m venv trading_env

# Activar entorno virtual
# Windows
trading_env\Scripts\activate
# Linux/macOS
source trading_env/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

### Configuración de API Keys

```bash
# Crear archivo de configuración de entorno
touch .env

# Editar con tus credenciales de Bybit
nano .env
```

**Archivo .env**:
```bash
# Bybit API Configuration
BYBIT_API_KEY=your_api_key_here
BYBIT_SECRET_KEY=your_secret_key_here
BYBIT_TESTNET=True  # True para testnet, False para producción

# Trading Configuration
DEFAULT_SYMBOL=BTCUSDT
DEFAULT_TIMEFRAME=240
DEFAULT_POSITION_SIZE=100
MAX_POSITIONS=3

# Risk Management
STOP_LOSS_PERCENTAGE=2.0
TAKE_PROFIT_PERCENTAGE=4.0
MAX_DRAWDOWN_PERCENTAGE=10.0

# Logging Configuration
LOG_LEVEL=INFO
LOG_FILE=trading_bot.log
```

### Configuración de Estrategias

```yaml
# config/config.yaml
trading:
  symbols:
    - BTCUSDT
    - ETHUSDT
    - ADAUSDT
  
  timeframes:
    - "240"  # 4 horas
    - "60"   # 1 hora
    - "15"   # 15 minutos
  
  indicators:
    ema:
      periods: [10, 55, 200]
    rsi:
      period: 14
      overbought: 70
      oversold: 30
    macd:
      fast: 12
      slow: 26
      signal: 9
    adx:
      period: 14
      threshold: 25

risk_management:
  max_risk_per_trade: 0.02  # 2% del capital
  max_open_positions: 3
  stop_loss: 0.02  # 2%
  take_profit: 0.04  # 4%
```

## 🚀 Uso del Bot

### Ejecución Básica

```bash
# Ejecutar el bot principal
python src/main.py

# Ejecutar con configuración específica
python src/main.py --config config/config.yaml

# Modo demo (testnet)
python src/main.py --demo

# Modo backtesting
python src/main.py --backtest --start-date 2024-01-01 --end-date 2024-12-31
```

### Análisis de Mercado

```python
# Ejemplo de uso básico
from src.exchange.bybit_client import BybitClient
from src.indicators.technical_indicators import *

# Inicializar cliente
client = BybitClient()

# Obtener datos de mercado
symbol = "BTCUSDT"
timeframe = "240"  # 4 horas
limit = 1000

cierres, altos, bajos = client.get_candles(symbol, timeframe, limit)

# Calcular indicadores
ema_10 = calcular_ema(cierres, 10)
ema_55 = calcular_ema(cierres, 55)
ema_200 = calcular_ema(cierres, 200)

rsi_14 = calcular_rsi(cierres, 14)
macd_line, signal_line, histogram = calcular_macd(cierres)
adx_14 = calcular_adx(cierres, altos, bajos, 14)

print(f"Precio actual: {cierres[-1]}")
print(f"EMA 10: {ema_10[-1]}")
print(f"RSI 14: {rsi_14[-1]}")
print(f"ADX 14: {adx_14[-1]}")
```

### Ejecución de Estrategias

```python
# Ejemplo de estrategia simple
from src.strategies.tradinglatino_strategy import TradingLatinoStrategy

# Inicializar estrategia
strategy = TradingLatinoStrategy()

# Evaluar señales de trading
signal = strategy.evaluate_signals(cierres, altos, bajos)

if signal == "BUY":
    print("Señal de compra detectada")
    # Ejecutar orden de compra
elif signal == "SELL":
    print("Señal de venta detectada")
    # Ejecutar orden de venta
else:
    print("No hay señales de trading")
```

### Gestión de Posiciones

```python
from src.exchange.trading import abrir_posicion, cerrar_posicion

# Abrir posición de compra
symbol = "BTCUSDT"
quantity = 0.001  # BTC
side = "Buy"

resultado = abrir_posicion(symbol, quantity, side)
print(f"Posición abierta: {resultado}")

# Cerrar posición
resultado_cierre = cerrar_posicion(symbol, quantity, "Sell")
print(f"Posición cerrada: {resultado_cierre}")
```

## 📁 Estructura del Proyecto

```
bot/
├── requirements.txt                      # Dependencias del proyecto
├── pytest.ini                          # Configuración de testing
├── .gitignore                           # Archivos ignorados por Git
├── README.md                            # Documentación principal
├── config/                              # Configuraciones
│   └── config.yaml                      # Configuración principal
├── notebooks/                           # Jupyter notebooks
│   └── exploration.ipynb                # Análisis exploratorio
├── src/                                 # Código fuente principal
│   ├── __init__.py                      # Inicialización del paquete
│   ├── main.py                          # Punto de entrada principal
│   ├── exchange/                        # Conectores de exchange
│   │   ├── __init__.py                  # Inicialización del módulo
│   │   ├── bybit_client.py              # Cliente principal de Bybit
│   │   ├── bybit_exchange.py            # Conexión base con Bybit
│   │   └── trading.py                   # Funciones de trading
│   ├── indicators/                      # Indicadores técnicos
│   │   ├── __init__.py                  # Inicialización del módulo
│   │   └── technical_indicators.py      # Implementación de indicadores
│   ├── strategies/                      # Estrategias de trading
│   │   ├── __init__.py                  # Inicialización del módulo
│   │   └── tradinglatino_strategy.py    # Estrategia personalizada
│   ├── risk/                            # Gestión de riesgo
│   │   └── risk_management.py           # Módulos de gestión de riesgo
│   └── utils/                           # Utilidades generales
│       ├── data_utils.py                # Utilidades de datos
│       ├── logging_utils.py             # Sistema de logging
│       └── config_utils.py              # Gestión de configuración
└── test/                                # Suite de pruebas
    ├── test_indicators.py               # Tests de indicadores
    ├── test_strategies.py               # Tests de estrategias
    ├── test_exchange.py                 # Tests de conectividad
    └── test_risk.py                     # Tests de gestión de riesgo
```

## 📊 Indicadores Técnicos Implementados

### Moving Averages (Medias Móviles)

**Exponential Moving Average (EMA)**:
```python
def calcular_ema(cierres, periodo):
    """
    Calcula la EMA para identificar tendencias y puntos de entrada.
    
    Parámetros:
    - cierres: Lista de precios de cierre
    - periodo: Período de la EMA (ej: 10, 55, 200)
    
    Uso:
    - EMA 10 > EMA 55: Tendencia alcista a corto plazo
    - EMA 55 > EMA 200: Tendencia alcista a largo plazo
    - Crossover: Señales de cambio de tendencia
    """
```

### Oscillators (Osciladores)

**Relative Strength Index (RSI)**:
```python
def calcular_rsi(cierres, periodo=14):
    """
    Oscilador de momentum para identificar condiciones de sobrecompra/sobreventa.
    
    Interpretación:
    - RSI > 70: Posible sobrecompra (señal de venta)
    - RSI < 30: Posible sobreventa (señal de compra)
    - RSI 50: Línea neutral
    """
```

**Stochastic Oscillator**:
```python
def calcular_estocastico(cierres, altos, bajos, k_periodo=14, d_periodo=3):
    """
    Compara el precio de cierre con el rango de precios durante un período.
    
    Señales:
    - %K > 80: Sobrecompra
    - %K < 20: Sobreventa
    - Crossover %K y %D: Señales de entrada/salida
    """
```

### Trend Indicators (Indicadores de Tendencia)

**Average Directional Index (ADX)**:
```python
def calcular_adx(cierres, altos, bajos, periodo=14):
    """
    Mide la fuerza de la tendencia sin indicar dirección.
    
    Interpretación:
    - ADX > 25: Tendencia fuerte
    - ADX < 20: Tendencia débil o rango lateral
    - ADX creciente: Fortalecimiento de tendencia
    """
```

**Moving Average Convergence Divergence (MACD)**:
```python
def calcular_macd(cierres, rapida=12, lenta=26, senal=9):
    """
    Indicador de momentum que muestra relación entre dos EMAs.
    
    Señales:
    - MACD cruza por encima de Signal: Posible compra
    - MACD cruza por debajo de Signal: Posible venta
    - Histograma positivo: Momentum alcista
    """
```

### Volume Indicators (Indicadores de Volumen)

**Volume Profile**:
```python
def calcular_volume_profile(cierres, volumenes, bins=20):
    """
    Muestra la distribución de volumen en diferentes niveles de precio.
    
    Uso:
    - Niveles de alto volumen: Soporte/resistencia
    - Point of Control (POC): Precio con mayor volumen
    - Value Area: Zona del 70% del volumen total
    """
```

### Advanced Indicators (Indicadores Avanzados)

**Squeeze Momentum Indicator**:
```python
def calcular_squeeze_momentum(cierres, altos, bajos):
    """
    Detecta períodos de baja volatilidad seguidos de movimientos explosivos.
    
    Estados:
    - Squeeze ON: Bandas de Bollinger dentro de Canales de Keltner
    - Squeeze OFF: Preparación para movimiento fuerte
    - Momentum: Dirección del movimiento esperado
    """
```

## 🔧 Desarrollo de Estrategias

### Framework de Estrategias

```python
# Plantilla base para estrategias personalizadas
class BaseStrategy:
    def __init__(self, config):
        self.config = config
        self.indicators = {}
        
    def calculate_indicators(self, cierres, altos, bajos):
        """Calcula todos los indicadores necesarios"""
        self.indicators['ema_10'] = calcular_ema(cierres, 10)
        self.indicators['ema_55'] = calcular_ema(cierres, 55)
        self.indicators['rsi'] = calcular_rsi(cierres, 14)
        self.indicators['adx'] = calcular_adx(cierres, altos, bajos, 14)
        
    def generate_signals(self):
        """Genera señales de compra/venta basadas en indicadores"""
        signals = []
        
        # Ejemplo: Estrategia de cruce de EMAs con confirmación de RSI
        if (self.indicators['ema_10'][-1] > self.indicators['ema_55'][-1] and
            self.indicators['ema_10'][-2] <= self.indicators['ema_55'][-2] and
            self.indicators['rsi'][-1] > 50 and
            self.indicators['adx'][-1] > 25):
            signals.append('BUY')
            
        elif (self.indicators['ema_10'][-1] < self.indicators['ema_55'][-1] and
              self.indicators['ema_10'][-2] >= self.indicators['ema_55'][-2] and
              self.indicators['rsi'][-1] < 50 and
              self.indicators['adx'][-1] > 25):
            signals.append('SELL')
            
        return signals
        
    def execute_strategy(self, cierres, altos, bajos):
        """Ejecuta la estrategia completa"""
        self.calculate_indicators(cierres, altos, bajos)
        return self.generate_signals()
```

### Estrategia de Trading Multi-timeframe

```python
class MultiTimeframeStrategy(BaseStrategy):
    def __init__(self, config):
        super().__init__(config)
        self.timeframes = ['240', '60', '15']  # 4h, 1h, 15m
        
    def analyze_timeframes(self, symbol):
        """Analiza múltiples marcos temporales para confirmación"""
        signals = {}
        
        for tf in self.timeframes:
            cierres, altos, bajos = self.client.get_candles(symbol, tf, 200)
            tf_signals = self.execute_strategy(cierres, altos, bajos)
            signals[tf] = tf_signals
            
        # Lógica de confirmación entre timeframes
        if all('BUY' in signals[tf] for tf in self.timeframes):
            return 'STRONG_BUY'
        elif signals['240'] == ['BUY'] and signals['60'] == ['BUY']:
            return 'BUY'
        elif all('SELL' in signals[tf] for tf in self.timeframes):
            return 'STRONG_SELL'
        elif signals['240'] == ['SELL'] and signals['60'] == ['SELL']:
            return 'SELL'
        else:
            return 'HOLD'
```

## 🧪 Testing y Backtesting

### Testing Unitario

```bash
# Ejecutar todos los tests
pytest

# Ejecutar tests específicos
pytest test/test_indicators.py
pytest test/test_strategies.py

# Ejecutar tests con coverage
pytest --cov=src

# Ejecutar tests con output detallado
pytest -v
```

### Backtesting Framework

```python
# Ejemplo de backtesting
from src.backtesting.backtest_engine import BacktestEngine

# Configurar backtesting
backtest = BacktestEngine(
    symbol='BTCUSDT',
    timeframe='240',
    start_date='2024-01-01',
    end_date='2024-12-31',
    initial_capital=10000
)

# Añadir estrategia
backtest.add_strategy(TradingLatinoStrategy())

# Ejecutar backtesting
results = backtest.run()

# Analizar resultados
print(f"Retorno total: {results['total_return']:.2%}")
print(f"Sharpe ratio: {results['sharpe_ratio']:.2f}")
print(f"Máximo drawdown: {results['max_drawdown']:.2%}")
print(f"Número de trades: {results['total_trades']}")
print(f"Win rate: {results['win_rate']:.2%}")
```

### Métricas de Performance

```python
def calculate_performance_metrics(trades):
    """
    Calcula métricas de rendimiento del bot.
    """
    metrics = {
        'total_trades': len(trades),
        'winning_trades': len([t for t in trades if t['pnl'] > 0]),
        'losing_trades': len([t for t in trades if t['pnl'] < 0]),
        'win_rate': len([t for t in trades if t['pnl'] > 0]) / len(trades),
        'total_pnl': sum([t['pnl'] for t in trades]),
        'average_win': np.mean([t['pnl'] for t in trades if t['pnl'] > 0]),
        'average_loss': np.mean([t['pnl'] for t in trades if t['pnl'] < 0]),
        'profit_factor': abs(sum([t['pnl'] for t in trades if t['pnl'] > 0]) / 
                           sum([t['pnl'] for t in trades if t['pnl'] < 0])),
        'max_consecutive_wins': calculate_max_consecutive(trades, 'win'),
        'max_consecutive_losses': calculate_max_consecutive(trades, 'loss')
    }
    return metrics
```

## 🛡️ Gestión de Riesgo Avanzada

### Position Sizing (Tamaño de Posición)

```python
class RiskManager:
    def __init__(self, config):
        self.max_risk_per_trade = config['max_risk_per_trade']
        self.max_portfolio_risk = config['max_portfolio_risk']
        
    def calculate_position_size(self, account_balance, entry_price, stop_loss_price):
        """
        Calcula el tamaño de posición basado en el riesgo por trade.
        
        Formula: Position Size = (Account Balance * Risk %) / (Entry Price - Stop Loss Price)
        """
        risk_amount = account_balance * self.max_risk_per_trade
        price_difference = abs(entry_price - stop_loss_price)
        
        if price_difference == 0:
            return 0
            
        position_size = risk_amount / price_difference
        return round(position_size, 6)
        
    def validate_trade(self, proposed_trade, current_positions):
        """
        Valida si el trade propuesto cumple con las reglas de riesgo.
        """
        # Verificar riesgo por trade
        if proposed_trade['risk'] > self.max_risk_per_trade:
            return False, "Riesgo por trade excede el límite"
            
        # Verificar riesgo total del portfolio
        total_risk = sum([pos['risk'] for pos in current_positions])
        if total_risk + proposed_trade['risk'] > self.max_portfolio_risk:
            return False, "Riesgo total del portfolio excede el límite"
            
        return True, "Trade aprobado"
```

### Stop Loss Dinámico

```python
class DynamicStopLoss:
    def __init__(self, initial_stop_percentage=0.02):
        self.initial_stop_percentage = initial_stop_percentage
        
    def calculate_trailing_stop(self, entry_price, current_price, side, trail_percentage=0.01):
        """
        Calcula stop loss dinámico que sigue al precio favorable.
        """
        if side == "Buy":
            # Para posiciones largas
            initial_stop = entry_price * (1 - self.initial_stop_percentage)
            if current_price > entry_price:
                # Precio favorable, actualizar stop loss
                trailing_stop = current_price * (1 - trail_percentage)
                return max(initial_stop, trailing_stop)
            else:
                return initial_stop
        else:
            # Para posiciones cortas
            initial_stop = entry_price * (1 + self.initial_stop_percentage)
            if current_price < entry_price:
                # Precio favorable, actualizar stop loss
                trailing_stop = current_price * (1 + trail_percentage)
                return min(initial_stop, trailing_stop)
            else:
                return initial_stop
```

## 🚨 Resolución de Problemas

### Problemas Comunes

**Error de conexión con API**:
```bash
# Verificar credenciales
echo $BYBIT_API_KEY
echo $BYBIT_SECRET_KEY

# Verificar conectividad
python -c "from src.exchange.bybit_client import BybitClient; client = BybitClient(); print(client.get_balance())"

# Verificar permisos de API
# Asegúrate de que tu API key tenga permisos de trading activados
```

**Errores de indicadores técnicos**:
```bash
# Verificar datos de entrada
python -c "
from src.exchange.bybit_client import BybitClient
client = BybitClient()
cierres, altos, bajos = client.get_candles('BTCUSDT', '240', 100)
print(f'Datos obtenidos: {len(cierres)} velas')
print(f'Último cierre: {cierres[-1] if cierres else None}')
"

# Verificar dependencias
pip install --upgrade ta numpy pandas
```

**Problemas de ejecución de órdenes**:
```bash
# Verificar saldo disponible
python -c "
from src.exchange.bybit_client import BybitClient
client = BybitClient()
client.get_saldo()
"

# Verificar configuración de testnet
# Asegúrate de estar usando testnet para pruebas
```

### Debugging y Logging

```python
import logging

# Configurar logging detallado
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('trading_bot_debug.log'),
        logging.StreamHandler()
    ]
)

# Usar logging en el bot
logger = logging.getLogger(__name__)

def debug_trading_decision(indicators, signals):
    """
    Registra información detallada sobre decisiones de trading.
    """
    logger.info(f"Indicadores actuales: {indicators}")
    logger.info(f"Señales generadas: {signals}")
    logger.debug(f"Lógica de decisión ejecutada")
```

### Optimización de Performance

```python
# Optimizar obtención de datos
async def get_multiple_candles_async(symbols, timeframe):
    """
    Obtiene datos de múltiples símbolos de forma asíncrona.
    """
    import asyncio
    
    async def get_candles_async(symbol):
        # Implementar obtención asíncrona
        pass
    
    tasks = [get_candles_async(symbol) for symbol in symbols]
    results = await asyncio.gather(*tasks)
    return results

# Cachear cálculos de indicadores
from functools import lru_cache

@lru_cache(maxsize=100)
def cached_indicator_calculation(prices_tuple, indicator_type, period):
    """
    Cache de cálculos de indicadores para evitar recomputación.
    """
    prices = list(prices_tuple)
    if indicator_type == 'ema':
        return calcular_ema(prices, period)
    elif indicator_type == 'rsi':
        return calcular_rsi(prices, period)
    # ... otros indicadores
```

## 📈 Características Avanzadas

### Machine Learning Integration

```python
# Preparación para integración con ML
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

class MLStrategy(BaseStrategy):
    def __init__(self, config):
        super().__init__(config)
        self.model = None
        self.scaler = StandardScaler()
        
    def prepare_features(self, cierres, altos, bajos):
        """
        Prepara características para modelo de ML.
        """
        features = pd.DataFrame({
            'ema_10': calcular_ema(cierres, 10),
            'ema_55': calcular_ema(cierres, 55),
            'rsi': calcular_rsi(cierres, 14),
            'adx': calcular_adx(cierres, altos, bajos, 14),
            'price_change': [0] + [cierres[i]/cierres[i-1] - 1 for i in range(1, len(cierres))]
        })
        return features.dropna()
        
    def train_model(self, historical_data, labels):
        """
        Entrena modelo de ML con datos históricos.
        """
        X = self.scaler.fit_transform(historical_data)
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X, labels)
        
    def predict_signal(self, current_features):
        """
        Predice señal usando modelo entrenado.
        """
        if self.model is None:
            return 'HOLD'
            
        X = self.scaler.transform([current_features])
        prediction = self.model.predict(X)[0]
        confidence = max(self.model.predict_proba(X)[0])
        
        if confidence > 0.7:  # Umbral de confianza
            return ['HOLD', 'BUY', 'SELL'][prediction]
        else:
            return 'HOLD'
```

### Portfolio Management

```python
class PortfolioManager:
    def __init__(self, config):
        self.symbols = config['symbols']
        self.allocation = config['allocation']
        self.rebalance_threshold = config['rebalance_threshold']
        
    def calculate_portfolio_weights(self, current_prices):
        """
        Calcula pesos actuales del portfolio.
        """
        total_value = sum([self.positions[symbol] * current_prices[symbol] 
                          for symbol in self.symbols])
        
        weights = {symbol: (self.positions[symbol] * current_prices[symbol]) / total_value 
                  for symbol in self.symbols}
        return weights
        
    def rebalance_portfolio(self, target_weights, current_weights):
        """
        Rebalancea el portfolio hacia los pesos objetivo.
        """
        rebalance_actions = []
        
        for symbol in self.symbols:
            weight_diff = target_weights[symbol] - current_weights[symbol]
            
            if abs(weight_diff) > self.rebalance_threshold:
                action = 'BUY' if weight_diff > 0 else 'SELL'
                quantity = abs(weight_diff) * self.total_portfolio_value / current_prices[symbol]
                
                rebalance_actions.append({
                    'symbol': symbol,
                    'action': action,
                    'quantity': quantity,
                    'reason': 'rebalance'
                })
                
        return rebalance_actions
```

### Real-time Data Streaming

```python
import websocket
import json
import threading

class RealTimeDataStreamer:
    def __init__(self, symbols, callback):
        self.symbols = symbols
        self.callback = callback
        self.ws = None
        
    def on_message(self, ws, message):
        """
        Procesa mensajes en tiempo real del WebSocket.
        """
        data = json.loads(message)
        
        if 'kline' in data:
            symbol = data['symbol']
            kline = data['kline']
            
            # Procesar datos de vela en tiempo real
            processed_data = {
                'symbol': symbol,
                'timestamp': kline['timestamp'],
                'open': float(kline['open']),
                'high': float(kline['high']),
                'low': float(kline['low']),
                'close': float(kline['close']),
                'volume': float(kline['volume'])
            }
            
            # Llamar callback con datos procesados
            self.callback(processed_data)
            
    def start_streaming(self):
        """
        Inicia stream de datos en tiempo real.
        """
        def run_websocket():
            self.ws = websocket.WebSocketApp(
                "wss://stream.bybit.com/v5/public/linear",
                on_message=self.on_message,
                on_error=self.on_error,
                on_close=self.on_close
            )
            
            # Suscribirse a símbolos
            subscribe_msg = {
                "op": "subscribe",
                "args": [f"kline.240.{symbol}" for symbol in self.symbols]
            }
            
            self.ws.on_open = lambda ws: ws.send(json.dumps(subscribe_msg))
            self.ws.run_forever()
            
        thread = threading.Thread(target=run_websocket, daemon=True)
        thread.start()
```

## 👨‍💻 Autores

**Desarrollador Principal:**
- **Rubén Delicado** - [@rdelicado](https://github.com/rdelicado)
  - 📧 rdelicad@student.42malaga.com
  - 🏫 42 Málaga
  - 🤖 Especialista en Trading Algorítmico

**Áreas de Especialización:**
- **Quantitative Finance**: Análisis cuantitativo y desarrollo de estrategias
- **Algorithmic Trading**: Automatización de sistemas de trading
- **Technical Analysis**: Implementación de indicadores técnicos avanzados
- **Risk Management**: Sistemas de gestión de riesgo y capital
- **API Integration**: Integración con exchanges de criptomonedas
- **Python Development**: Desarrollo especializado en fintech

## 📜 Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles.

**Aviso Legal**: Este software es solo para fines educativos y de investigación. El trading de criptomonedas conlleva riesgos significativos y puede resultar en pérdidas financieras. Los desarrolladores no son responsables de las pérdidas incurridas por el uso de este bot.

## 🔗 Recursos y Referencias

### Trading y Finanzas
- [Bybit API Documentation](https://bybit-exchange.github.io/docs/v5/intro)
- [CCXT Documentation](https://docs.ccxt.com/)
- [TA-Lib Technical Analysis](https://ta-lib.org/)
- [Quantitative Trading Strategies](https://www.quantstart.com/)

### Análisis Técnico
- [TradingView Indicators](https://www.tradingview.com/pine-script-docs/)
- [Technical Analysis Library](https://technical-analysis-library-in-python.readthedocs.io/)
- [Pandas TA Documentation](https://github.com/twopirllc/pandas-ta)
- [Technical Analysis Patterns](https://www.investopedia.com/technical-analysis-4689657)

### Python y Desarrollo
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Asyncio Documentation](https://docs.python.org/3/library/asyncio.html)
- [Python Testing with Pytest](https://docs.pytest.org/)

### Gestión de Riesgo
- [Risk Management in Trading](https://www.investopedia.com/articles/trading/09/risk-management.asp)
- [Position Sizing Strategies](https://www.investopedia.com/articles/trading/09/position-size.asp)
- [Portfolio Theory](https://www.investopedia.com/terms/m/modernportfoliotheory.asp)

## 🚀 Roadmap y Extensiones Futuras

### Características Planeadas
- [ ] **Machine Learning Integration**: Modelos predictivos con scikit-learn
- [ ] **Multi-Exchange Support**: Soporte para Binance, OKX, KuCoin
- [ ] **Advanced Strategies**: Arbitraje, market making, grid trading
- [ ] **Web Dashboard**: Interfaz web para monitoreo y control
- [ ] **Mobile Notifications**: Alertas push en dispositivos móviles
- [ ] **Social Trading**: Copia de operaciones de traders exitosos

### Mejoras Técnicas
- [ ] **Kubernetes Deployment**: Despliegue escalable en la nube
- [ ] **Real-time Analytics**: Dashboard en tiempo real con Grafana
- [ ] **Database Integration**: Almacenamiento de datos históricos con PostgreSQL
- [ ] **API REST**: API para integración con aplicaciones externas
- [ ] **Backtesting Engine**: Motor de backtesting más robusto
- [ ] **Paper Trading**: Modo de trading simulado avanzado

### Estrategias Avanzadas
- [ ] **Mean Reversion**: Estrategias de reversión a la media
- [ ] **Momentum Trading**: Estrategias basadas en momentum
- [ ] **Arbitrage Bot**: Bot de arbitraje entre exchanges
- [ ] **DCA Bot**: Dollar Cost Averaging automatizado
- [ ] **Grid Trading**: Trading de grilla automatizado
- [ ] **News Sentiment**: Trading basado en sentimiento de noticias

---

<div align="center">

*"En el trading algorítmico, la precisión técnica y la gestión disciplinada del riesgo son los pilares fundamentales del éxito sostenible en los mercados financieros."*

**Crypto Trading Bot** demuestra que la combinación de análisis técnico avanzado, gestión de riesgo sofisticada y automatización inteligente puede crear sistemas de trading robustos y eficientes para los mercados de criptomonedas.

</div>