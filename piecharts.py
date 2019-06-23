import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
sleeping = [7, 6, 8, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]

slices = [7, 2, 2, 13]
activities = ['sleeping', 'eating', 'working', 'playing']
colors = ['c', 'm', 'r', 'b']

# startangle - градус с которого начинается наш график
# shadow - добавляет типо 3д эфект
# explode - отрывает части от цельного графика
# autopct - в процентном соотношении показывает части графика
plt.pie(slices,
        labels=activities,
        colors=colors,
        startangle=90,
        shadow=True,
        explode=(0.1, 0.2, 0, 0),
        autopct='%1.1f%%')


# название нашего графика
plt.title('Interesting graph\nCheck it out')
plt.show()