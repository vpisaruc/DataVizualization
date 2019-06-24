import pandas as pd
import matplotlib.pyplot as plt
import requests
import pandas_datareader.data as web
import datetime as dt

start = dt.datetime(2000, 1, 1)
end = dt.datetime(2016, 12,  31)

df = web.DataReader('TSLA', 'yahoo', start, end)

high = df[['High']]
low = df[['Low']]
open = df[['Open']]
close = df[['Close']]
volume = df[['Volume']]
adj_close = df[['Adj Close']]

fig = plt.figure()
ax1 = plt.subplot2grid((1, 1), (0, 0))

ax1.plot(high, label='Price')
# делаем разворот дат на 45град
for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(45)

# включаем сетку позади графика
ax1.grid(True)

plt.xlabel('Date')
plt.ylabel('Prices')
plt.legend()
# задание отступов от самой картинки до рамки
plt.subplots_adjust(left=0.09, bottom=0.18, right=0.94, top=0.90, wspace=0.2, hspace=0)
plt.show()
