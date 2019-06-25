from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

x = [1, 2, 3, 4, 5]
y = [4, 5, 1, 7, 5]
z = np.zeros(5)

dx = np.ones(5)
dy = np.ones(5)
dz = [1, 2, 3, 4, 5]

ax1.bar3d(x, y, z, dx, dy, dz)
x2 = [[-1, -2, -3, -4, -5]]
y2 = [[-4, -5, -1, -7, -5]]
z2 = [[-1, -5, -9, -5, -2]]

ax1.plot_wireframe(np.array(x2), np.array(y2), np.array(z2))

ax1.scatter(x, y, z)
ax1.scatter(x2, y2, z2)

ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')

plt.show()