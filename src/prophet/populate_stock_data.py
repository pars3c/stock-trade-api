import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prophet.settings')
import django

django.setup()

from stockDataCollector.models import stockData
from datetime import datetime
import requests
import json

def adding_to_db(symbol_trade, date_trade, open_trade, close_trade, low_trade, high_trade, volume_trade):
        if (stockData.objects.filter(symbol_trade=symbol_trade, date_trade=date_trade, open_trade=open_trade, 
                close_trade=close_trade, low_trade=low_trade, high_trade=high_trade, volume_trade=volume_trade).exists()):
                print("nothing can be done")
        else:
                p = stockData(symbol_trade='MSFTs2', date_trade="2018-11-02 16:00:00", open_trade=106.0100, close_trade=106.1400, low_trade=105.9100, high_trade=106.1900, volume_trade=825557)
                p.save()

def api_extraction(symbol):
        API_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=' + symbol + '&interval=1min&apikey=ZQ39SRI4010VT4OS&datatype=json'
        

if __name__ == "__main__":
    api_extraction()
    #adding_to_db(symbol_trade='MSFTs23', date_trade="2018-11-02 16:00:00", open_trade=106.0100, close_trade=106.1400, low_trade=105.9100, high_trade=106.1900, volume_trade=825557)