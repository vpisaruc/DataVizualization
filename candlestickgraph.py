import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
import  datetime
import pandas_datareader.data as web
from pandas.plotting import register_matplotlib_converters
import datetime as dt

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
df = df[:100]

# конвертируем колонку дат в формат матплотлиба
df['Date'] = df['Date'].map(lambda x: mdates.datestr2num(x))

fig = plt.figure()
ax1 = plt.subplot2grid((1, 1), (0, 0))

# делаем наш candlestick график
candlestick_ohlc(ax1, df.values, width=0.4, colorup='g', colordown='r')

for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(45)

# изменили формат дат с ужасного на нормальный
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
# сколько дат будет показанно по оси X
ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
ax1.grid(True)

plt.xlabel('Date')
plt.ylabel('Prices')
plt.title(stock)
plt.legend()
# задание отступов от самой картинки до рамки
plt.subplots_adjust(left=0.09, bottom=0.18, right=0.94, top=0.90, wspace=0.2, hspace=0)
plt.show()
