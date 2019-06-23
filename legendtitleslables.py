import matplotlib.pyplot as plt

# наши данные
x = [1, 2, 3]
y = [5, 7, 4]
# добавим больше данных
x2 = [1, 2, 3]
y2 = [10, 14, 12]

# собственно график, который мы будем настраивать
plt.plot(x, y, label='First Line')
# добавим еще график
# поле label используется для последующего отображения в legend
plt.plot(x2, y2, label='Second Line')
# настраиваем лэйблы под осями x и y
plt.xlabel('Plot number')
plt.ylabel('Important var')

plt.legend()
# название нашего графика
plt.title('Interesting graph\nCheck it out')
plt.show()