

import matplotlib.pyplot as plt
import numpy as np

# Paramètres de la figure
fig = plt.figure(figsize=(5,5))
ax = fig.add_subplot(1,1,1, projection='3d')

# Paramètres des sphères
r_big = 1
r_small = 0.25

# Paramètres des angles
theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
phi = np.linspace(0, 2 * np.pi, 100)

# Coordonnées des sphères
x_big = r_big * np.outer(np.cos(theta), np.sin(phi))
y_big = r_big * np.outer(np.sin(theta), np.sin(phi))
z_big = r_big * np.outer(np.ones(np.size(theta)), np.cos(phi))

x_small = r_small * np.outer(np.cos(theta), np.sin(phi)) + 1
y_small = r_small * np.outer(np.sin(theta), np.sin(phi))
z_small = r_small * np.outer(np.ones(np.size(theta)), np.cos(phi))

# Dessin des sphères
ax.plot_surface(x_big, y_big, z_big, color="red", alpha=0.5)
ax.plot_surface(x_small, y_small, z_small, color="blue", alpha=0.5)

# Ajustement des axes
ax.set_xlim(-2,2)
ax.set_ylim(-2,2)
ax.set_zlim(-2,2)

# Affichage du graphique
plt.show()