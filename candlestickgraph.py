import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
import datetime as dt
import pandas_datareader as web
from mpl_finance import candlestick_ohlc
from matplotlib import style
from pandas.plotting import register_matplotlib_converters

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

# настройки bbox
bbox_props = dict(boxstyle='round', fc='w', ec='k', lw=1)

# аннотация последней цены сбоку
ax1.annotate(str(df['Close'].values[-1]),
             (df['Date'].values[-1], df['Close'].values[-1]),
             xytext=(df['Date'].values[-1] + 6, df['Close'].values[-1]),
             bbox=bbox_props)

# Annotation example
# первые координаты это координаты события которое мы комментируем
# xytext - расположение текста в графике
# textcoords - мы показываем, что нашими координатыми будет процент от графика
# arrowprops настройки стрелки которая показывает от стрелки к событию
# ax1.annotate('Big News',
#              (df['Date'].values[13], df['High'].values[12]),
#              xytext=(0.3, 0.9),
#              textcoords='axes fraction',
#              arrowprops=dict(facecolor='grey', color='grey'))
#
# # прописываем стиль текста
# font_dict = {'family' : 'serif',
#              'color' : 'darkred',
#              'size' : 15}
# # ужасный способ вставки текста на график
# ax1.text(df['Date'].values[10], df['Close'].values[1], 'Text Example', fontdict=font_dict)

plt.xlabel('Date')
plt.ylabel('Prices')
plt.title(stock)
#plt.legend()
# задание отступов от самой картинки до рамки
plt.subplots_adjust(left=0.1, bottom=0.28, right=0.90, top=0.90, wspace=0.2, hspace=0)
plt.show()
