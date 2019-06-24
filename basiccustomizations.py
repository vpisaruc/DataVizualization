import pandas as pd
import matplotlib.pyplot as plt
import requests
import pandas_datareader.data as web
import datetime as dt
from pandas.plotting import register_matplotlib_converters

# чтобы не было warning
register_matplotlib_converters()

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2016, 12,  31)
stock = 'EBAY'

df = web.DataReader(stock, 'yahoo', start, end)

high = df[['High']]
low = df[['Low']]
open = df[['Open']]
close = df[['Close']]
volume = df[['Volume']]
adj_close = df[['Adj Close']]


fig = plt.figure()
ax1 = plt.subplot2grid((1, 1), (0, 0))

# чтобы отображалась линия графика при заливке
ax1.plot(high, label='Price', linewidth=0.2)
# для легенды
ax1.plot([], [], label='loss', linewidth=0.5, color='r', alpha=0.5)
ax1.plot([], [], label='gain', linewidth=0.5, color='g', alpha=0.5)

# залитый график
# alpha - прозрачность заливки
# значение посеридине это значение от которого начинается заливка
# were - задаем значения которые будут закрашены
ax1.fill_between(high.index,
                 high['High'],
                 high['High'][0],
                 where=(high['High'] > high['High'][0]),
                 facecolor='g',
                 alpha=1)

ax1.fill_between(high.index,
                 high['High'],
                 high['High'][0],
                 where=(high['High'] < high['High'][0]),
                 facecolor='r',
                 alpha=1)

# делаем разворот дат на 45град
for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(45)

# включаем сетку позади графика
ax1.grid(True)
# меняем цвет лэйблов
ax1.xaxis.label.set_color('c')
ax1.yaxis.label.set_color('r')
# шаг по оси y
ax1.set_yticks([0, 10, 20, 30, 40, 50])

plt.xlabel('Date')
plt.ylabel('Prices')
plt.title(stock)
plt.legend()
# задание отступов от самой картинки до рамки
plt.subplots_adjust(left=0.09, bottom=0.18, right=0.94, top=0.90, wspace=0.2, hspace=0)
plt.show()
