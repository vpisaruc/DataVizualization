import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import datetime as dt
import pandas_datareader as web
from mpl_finance import candlestick_ohlc
from matplotlib import style
from pandas.plotting import register_matplotlib_converters
import numpy as np

# окна для скользящей средней
MA1 = 10
MA2 = 30

"""функция для вычисления скользящей средней"""
def moving_average(values, window):
    weight = np.repeat(1.0, window) / window
    smas = np.convolve(values, weight, 'valid')
    return smas

def high_minus_low(highs, lows):
    return highs - lows

# сделаем наш график красивее
style.use('fivethirtyeight')
# распечатать все доступные стили
#print(plt.style.available)
# узнать где наша библиотека хранится
#print(plt.__file__)
# чтобы не было warning
register_matplotlib_converters()

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2016, 12,  31)
stock = 'EBAY'

#df = web.DataReader(stock, 'yahoo', start, end)
#df.to_csv('Datasets/dataset.csv')
df = pd.read_csv('Datasets/dataset.csv')
# удаляем ненужную колонку
df.drop(columns='Adj Close')
# делаем списко с нужным порядком колонок
cols = ['Date', 'Open', 'High', 'Low',  'Close', 'Volume']
# меняем порядок колонок
df = df[cols]
df = df[:500]

# конвертируем колонку дат в формат матплотлиба
df['Date'] = df['Date'].map(lambda x: mdates.datestr2num(x))

fig = plt.figure()
ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=1, colspan=1)
plt.title(stock)
ax2 = plt.subplot2grid((6, 1), (1, 0), rowspan=4, colspan=1)
plt.xlabel('Date')
plt.ylabel('Prices')
ax3 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1)

ma1 = moving_average(df['Close'].values, MA1)
ma2 = moving_average(df['Close'].values, MA2)
start = len(df['Date'].values[MA2 - 1:])

h_l = list(map(high_minus_low, df['High'].values, df['Low'].values))

ax1.plot_date(df['Date'].values, h_l, '-')

# делаем наш candlestick график
candlestick_ohlc(ax2, df.values, width=0.4, colorup='g', colordown='r')

for label in ax2.xaxis.get_ticklabels():
    label.set_rotation(45)

# изменили формат дат с ужасного на нормальный
ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
# сколько дат будет показанно по оси X
ax2.xaxis.set_major_locator(mticker.MaxNLocator(10))
ax2.grid(True)

# настройки bbox
bbox_props = dict(boxstyle='round', fc='w', ec='k', lw=1)

# аннотация последней цены сбоку
ax2.annotate(str(df['Close'].values[-1]),
             (df['Date'].values[-1], df['Close'].values[-1]),
             xytext=(df['Date'].values[-1] + 6, df['Close'].values[-1]),
             bbox=bbox_props)

ax3.plot(df['Date'].values[-start:], ma1[-start:])
ax3.plot(df['Date'].values[-start:], ma2[-start:])

#plt.legend()
# задание отступов от самой картинки до рамки
plt.subplots_adjust(left=0.1, bottom=0.28, right=0.90, top=0.90, wspace=0.2, hspace=0)
plt.show()
