import matplotlib.pyplot as plt

# пример графиков типа bar
"""
# наши данные
x = [2, 4, 6, 8, 10]
y = [6, 7, 8, 2, 4]

x2 = [1, 3, 5, 7, 9]
y2 = [7, 8, 4, 2, 2]

# столбиковый график
plt.bar(x, y, label='Bar 1', color='r')
plt.bar(x2, y2, label='Bar 2', color='c')
"""

# пример гистограммы
# данные
population_ages = [1,22, 55, 62, 21, 34, 42, 52, 45, 78, 123, 54, 79, 12, 66, 77, 99, 88, 100]
#ids = [x for x in range(len(population_ages))]

# это наши бары, первый хранит 0-9 лет жителй, второй от 10-19 и т.д
bins = [0, 10, 20, 40, 50, 60, 70, 80, 90, 100, 120, 130]

plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

# настраиваем лэйблы под осями x и y
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
# название нашего графика
plt.title('Interesting graph\nCheck it out')
plt.show()