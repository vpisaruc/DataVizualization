import matplotlib.pyplot as plt
import numpy as np
import csv

# Часть 1
"""
x = []
y = []

with open('example.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x, y, label='loaded from file')
"""

# Часть 2
x, y = np.loadtxt('Datasets\example.csv', delimiter=',', unpack=True)

plt.plot(x, y)

# настраиваем лэйблы под осями x и y
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
# название нашего графика
plt.title('Interesting graph\nCheck it out')
plt.show()