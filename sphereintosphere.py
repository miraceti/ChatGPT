import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Make data
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 10 * np.outer(np.cos(u), np.sin(v))
y = 10 * np.outer(np.sin(u), np.sin(v))
z = 10 * np.outer(np.ones(np.size(u)), np.cos(v))

# Plot the surface
ax.plot_surface(x, y, z, color='b')

# Make data for outer sphere
u1 = np.linspace(0, 2 * np.pi, 100)
v1 = np.linspace(0, np.pi, 100)
x1 = 20 * np.outer(np.cos(u1), np.sin(v1))
y1 = 20 * np.outer(np.sin(u1), np.sin(v1))
z1 = 20 * np.outer(np.ones(np.size(u1)), np.cos(v1))

# Plot the surface
ax.plot_surface(x1, y1, z1, color='r')

plt.show()