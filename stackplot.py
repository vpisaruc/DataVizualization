import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
sleeping = [7, 6, 8, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

# пустые графики делаются для того, чтобы добавить лэйблы в легенду
# т.к в stackplot нельзя добавить лэйблы
# linewidth делает наши линии жирнее
plt.plot([], [], color='m', label='sleeping', linewidth=5)
plt.plot([], [], color='c', label='eating', linewidth=5)
plt.plot([], [], color='r', label='working', linewidth=5)
plt.plot([], [], color='k', label='playing', linewidth=5)

plt.stackplot(days, sleeping, eating, working, playing, colors=['m', 'c', 'r', 'k'])

# настраиваем лэйблы под осями x и y
plt.xlabel('Plot number')
plt.ylabel('Important var')
plt.legend()
# название нашего графика
plt.title('Interesting graph\nCheck it out')
plt.show()