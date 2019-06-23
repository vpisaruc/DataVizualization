import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 4, 2, 1, 4, 5, 2]

# s - размер маркера, marker - тип маркера
plt.scatter(x, y, label='skitscat', color = 'k', marker='*', s=100)

# настраиваем лэйблы под осями x и y
plt.xlabel('Plot number')
plt.ylabel('Important var')
plt.legend()
# название нашего графика
plt.title('Interesting graph\nCheck it out')
plt.show()