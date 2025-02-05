import requests
import pandas as pd

# Fetch XAU/USD Historical Data
def get_xauusd_data():
    klines = client.get_klines(symbol="XAUUSDT", interval=Client.KLINE_INTERVAL_1HOUR, limit=100)
    df = pd.DataFrame(klines, columns=["timestamp", "open", "high", "low", "close", "volume", "close_time", "quote_asset_volume", "trades", "taker_base", "taker_quote", "ignore"])
    df = df[["timestamp", "open", "high", "low", "close", "volume"]].astype(float)
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit='ms')
    return df