import numpy as np
import time
import telebot
from binance.client import Client
from config import API_KEY, BINANCE_API_KEY, BINANCE_SECRET_KEY, TELEGRAM_BOT_TOKEN, CHAT_ID
from data_fetcher import get_xauusd_data
from indicator import add_indicators
from model import preprocess_data 
from model import build_model
from signal_sender import send_signal


# Binance API Keys (Replace with your own)
client = Client(BINANCE_API_KEY, BINANCE_SECRET_KEY)
# Telegram Bot Token (Replace with your own)
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


# Main Loop
if __name__ == "__main__":
    while True:
        df = get_xauusd_data()
        df = add_indicators(df)
        data, scaler = preprocess_data(df)
        
        # AI Model Prediction (Placeholder, needs training data)
        model = build_model()
        signal = np.random.choice(["BUY", "SELL"])  # Replace with real prediction
        send_signal(f"AI Trading Bot Signal: {signal} on XAU/USD")
        
        print("Trade signal sent: ", signal)
        time.sleep(3600)  # Run every hour
