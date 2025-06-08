'''
Includes functions associated with problem 1, which reads:
    1. (Basic implementation of factorized solution.) Compute
       the potential described in Section 3 as a 3D plot,
       setting V_0=1. You'll have to truncate the series at some
       value of n, which I will call N. Leave N as a
       user-settable parameter, easily visible at the top of
       your code. Show that going to higher N better matches
       the boundary conditions. Which boundary condition in
       particulat gets better matched as N increases, and why?

'''

import numpy as np

def compute_potential(x, y, N, V0=1, L=np.pi):
    '''
    Computes the truncated series approximation for V(x,y).

    Parameters:
        x, y: np.ndarray
            Meshgrid arrays.
        N: int
            Number of Fourier terms to include (only odd n).
        V0: float
            Boundary value at y=0.
        L: float
            Width of the box in x.

    Returns:
        V: np.ndarray
            Potential evaluated on the meshgrid.
    '''
    V = np.zeros_like(x)
    for n in range(1, N + 1, 2):  # odd n only
        coeff = 4 * V0 / (n * np.pi)
        V += coeff * np.sin(n * np.pi * x / L) * np.exp(-n * np.pi * y / L)
    return V

