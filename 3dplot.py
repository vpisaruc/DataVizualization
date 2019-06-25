from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(111, projection='3d')

x = [[1, 2, 3, 4, 5]]
y = [[4, 5, 1, 7, 5]]
z = [[1, 5, 9, 5, 2]]

ax1.plot_wireframe(np.array(x), np.array(y), np.array(z))
ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')

plt.show()