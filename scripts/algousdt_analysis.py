import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from pathlib import Path
import backtrader as bt
import plotly.io as pio
import datetime

CRYPTO_DATA_CSV_PATH = Path('~/work/backtesting/data')
ALGOUSDT_CSV_FILE = CRYPTO_DATA_CSV_PATH / 'ALGOUSDT_MinuteBars.csv'

data_pd = pd.read_csv(ALGOUSDT_CSV_FILE)
data_pd = data_pd.drop(columns=['ignore', 'tb_base_av', 'tb_quote_av', 'quote_av', 'trades', 'close_time'])
data_pd['timestamp'] = data_pd['timestamp'].apply(lambda x: x.split('.')[0])
data_pd.timestamp = pd.to_datetime(data_pd.timestamp, format='%Y-%m-%d %H:%M:%S')



