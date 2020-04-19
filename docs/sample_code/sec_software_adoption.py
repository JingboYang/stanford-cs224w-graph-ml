import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D # <--- This is important for 3d plotting 




a = np.arange(0, 1, 0.1)
b = np.arange(0, 1, 0.1)
c = np.arange(0, 1.5, 0.1)


X, Y = np.meshgrid(a, b)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

n = 100

# eqs = np.zeros((len(a), len(b)))
for i, va in enumerate(a):
    for j, vb in enumerate(b):
        # eqs[i][j] = va + vb
        for k, vc in enumerate(c):

            if va + vb - vc > va and va + vb - vc > vb:
                ax.scatter(va, vb, vc, c='g', s=1)
            elif va >= vb:
                ax.scatter(va, vb, vc, c='r', s=1)
            else:
                ax.scatter(va, vb, vc, c='b', s=1)

# ax.plot_surface(X, Y, eqs)

ax.set_xlabel('a')
ax.set_ylabel('b')
ax.set_zlabel('c')

plt.gca().invert_yaxis()

plt.show()