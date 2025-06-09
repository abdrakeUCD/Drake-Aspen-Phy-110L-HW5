'''
Main file through which code is run.
'''

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from tqdm import tqdm

from problem_1 import compute_potential
from problem_2 import compute_electric_field, step_rk2, trace_field_line
from problem_3 import compute_exact_potential, compute_fractional_error

# --------------------------------------------------------------
#                           PROBLEM 1
# --------------------------------------------------------------

# init params
N  = 1000 # have done N = 10, 20, 100, 1000
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
print(f"Plot saved for problem 1 as plots/problem_1_potential_N{N}.png")


# --------------------------------------------------------------
#                           PROBLEM 2
# --------------------------------------------------------------


# initialize seed points (y approx 0 to avoid singularity at y = 0)
n_lines = 50
x_vals = np.linspace(0, L, n_lines)
starting_points = [(x, 0.001) for x in x_vals]  # slightly above y = 0

# define bounds for termination
bounds = (0, L, 0, 2 * L)

# define the field function
field_fn = lambda x, y: compute_electric_field(x, y, N=N, V0=V0, L=L)

# plot field lines (if you dont want to use tqdm)
'''
plt.figure(figsize=(8, 6))
for point in starting_points:
    xs, ys = trace_field_line(
        starting_point=point,
        field_fn=field_fn,
        step_size=0.01,
        max_steps=2000,
        bounds=bounds,
        propogation_coefficient=1  # move with the field
    )
    plt.plot(xs, ys, color="black", linewidth=0.7)
    #print(f"plotted field line started at {point}")
'''
# plot field lines (using tqdm for loading bar)
for point in tqdm(starting_points, desc="Problem 2: tracing field lines"):
    xs, ys = trace_field_line(
        starting_point=point,
        field_fn=field_fn,
        step_size=0.01,
        max_steps=2000,
        bounds=bounds,
        propogation_coefficient=1
    )
    plt.plot(xs, ys, color="black", linewidth=0.7)

plt.title(f"Electric Field Lines from y=0 Boundary (N={N})")
plt.xlabel("x")
plt.ylabel("y")
plt.xlim(0, L)
plt.ylim(0, 2 * L)
plt.grid(True)
plt.savefig(f"plots/problem_2_fieldlines_N{N}.png")
plt.close()
print(f"Plot saved for problem 2 as plots/problem_2_fieldlines_N{N}.png")


# --------------------------------------------------------------
#                           PROBLEM 3
# --------------------------------------------------------------

#                             ~~~~ 
#                              a. 
#                             ~~~~

# reuse same meshgrid
V_series = compute_potential(X, Y, N=N, V0=V0, L=L)
V_exact  = compute_exact_potential(X, Y, V0=V0, L=L)

frac_error = compute_fractional_error(V_series, V_exact)

# plot error map
plt.figure(figsize=(8, 6))
plt.imshow(frac_error,
           extent=[0, L, 0, 2 * L],
           origin='lower',
           cmap='plasma',
           aspect='auto')
plt.colorbar(label='Fractional Error')
plt.title(f'Fractional Error of Series vs Exact Potential (N={N})')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig(f"plots/problem_3a_frac_error_N{N}.png")
plt.close()
print(f"Plot saved for problem 3 as plots/problem_3a_frac_error_N{N}.png")
