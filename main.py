import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim3d(-1, 1)
ax.set_ylim3d(-1, 1)
ax.set_zlim3d(-1, 1)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Plot the axes
ax.plot([-1, 1], [0, 0], [0, 0], color='black')
ax.plot([0, 0], [-1, 1], [0, 0], color='black')
ax.plot([0, 0], [0, 0], [-1, 1], color='black')

# Plot the vectors
u = np.array([1, 0, 0])  # Red vector
v = np.array([0, 1, 0])  # Green vector
w = np.cross(u, v)       # Blue vector

origin = np.array([0, 0, 0])

ax.quiver(*origin, *u, color='red', pivot='tail')
ax.quiver(*origin, *v, color='green', pivot='tail')
ax.quiver(*origin, *w, color='blue', pivot='tail')

plt.show()

