
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Paramètres du tore
R = 1 # Rayon majeur
r = 0.5 # Rayon mineur
N = 100 # Nombre de points de discrétisation

# Calcul des points de discrétisation du tore
u = np.linspace(0, 2 * np.pi, N)
v = np.linspace(0, 2 * np.pi, N)

U, V = np.meshgrid(u, v)

# Calcul des coordonnées du tore
X = (R + r * np.cos(V)) * np.cos(U)
Y = (R + r * np.cos(V)) * np.sin(U)
Z = r * np.sin(V)

# Affichage du tore en 3D
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='RdYlBu')
plt.show()