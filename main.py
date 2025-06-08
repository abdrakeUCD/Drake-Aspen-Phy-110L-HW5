'''
Main file through which code is run.
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from problem_1 import compute_potential
 
# --------------------------------------------------------------
#                           PROBLEM 1
# --------------------------------------------------------------

# init params
N  = 20
V0 = 1
L  = np.pi

# create mesh
x = np.linspace(0, L, 300)
y = np.linspace(0, 2 * L, 300)
X, Y = np.meshgrid(x, y)

# compute
V = compute_potential(X, Y, N=N, V0=V0, L=L)

# plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
surf = ax.plot_surface(X, Y, V, cmap=cm.viridis)
ax.set_title(f"3D Potential Plot for N={N}")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("V(x, y)")
plt.tight_layout()
plt.savefig(f"plots/problem_1_potential_N{N}.png")
plt.close()


# --------------------------------------------------------------
#                           PROBLEM 2
# --------------------------------------------------------------




# --------------------------------------------------------------
#                           PROBLEM 3
# --------------------------------------------------------------

#                             ~~~~ 
#                              a. 
#                             ~~~~


#                             ~~~~ 
#                              b. 
#                             ~~~~


