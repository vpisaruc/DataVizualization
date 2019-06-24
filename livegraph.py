import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
"""Если будете добавлять значения в файл при включенной программе
   график будет обновляться динамически"""
style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)

def animate(i):
    graph_data = open(r'Datasets\example.txt', 'r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(x)
            ys.append(y)

    ax1.clear()
    ax1.plot(xs, ys)

# fig - куда мы выводим наш график
# animate - функция которая получает данные
# interval в миллисекундах
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()