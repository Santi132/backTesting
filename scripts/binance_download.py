import pandas as pd
from binance.client import Client
from pathlib import Path
import datetime
import json

BINANCE_PAIRS_JSON_PATH = "/Users/santiagogutierrez/work/backtesting/data/BinancePairs.json"

# YOUR API KEYS HERE
api_key = "20c1UNyto4xZemQUtJPnfnULopAAVCWbgVBmCTFvX0gjcQF5kcMasuBRab7FJ6YF"    #Enter your own API-key here
api_secret = "l04kgQNS1CK47TQi7Ogstq5GxtG7NcRHz8xUhbfpWSIAWYUaGgCGE01oxR4XD25V" #Enter your own API-secret here

bclient = Client(api_key=api_key, api_secret=api_secret)

start_date = datetime.datetime.strptime('1 Jan 2016', '%d %b %Y')
today = datetime.datetime.today()
DATA_DIR_PATH = Path('/Users/santiagogutierrez/work/backtesting/data')

def binanceBarExtractor(symbol):
    print('working...')
    filename = DATA_DIR_PATH / '{}_MinuteBars.csv'.format(symbol)

    print(f'downloading minute data for {symbol}')
    klines = bclient.get_historical_klines(symbol, Client.KLINE_INTERVAL_1MINUTE, start_date.strftime("%d %b %Y %H:%M:%S"), today.strftime("%d %b %Y %H:%M:%S"), 1000)
    data = pd.DataFrame(klines, columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume', 'close_time', 'quote_av', 'trades', 'tb_base_av', 'tb_quote_av', 'ignore' ])
    data['timestamp'] = pd.to_datetime(data['timestamp'], unit='ms')

    data.set_index('timestamp', inplace=True)
    data.to_csv(filename)
    print('finished!')


if __name__ == '__main__':
    # Obviously replace BTCUSDT with whichever symbol you want from binance
    # Wherever you've saved this code is the same directory you will find the resulting CSV file
    binanceBarExtractor('BTCUSDT')
    binanceBarExtractor('ALGOUSDT')
