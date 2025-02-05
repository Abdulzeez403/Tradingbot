import talib

# Generate Technical Indicators
def add_indicators(df):
    df["RSI"] = talib.RSI(df["close"], timeperiod=14)
    df["MACD"], df["MACD_signal"], _ = talib.MACD(df["close"], fastperiod=12, slowperiod=26, signalperiod=9)
    df["EMA"] = talib.EMA(df["close"], timeperiod=20)
    return df