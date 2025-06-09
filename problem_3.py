'''
Includes functions assockiated with problem 3, which reads:
    3. (Comparison to other methods.) You can't solve this
       example with the relaxation method, because you cannot
       track y\rightarrow\infty on a grid. So I will tell you
       that there happens to be an exact analytic solution
       for this problem:

       \[
       V(x,y)=\frac{2V_0}{\pi}\arctan\left(\frac{\sin\left(\frac{\pi x}{L}\right)}{\sinh\left(\frac{\pi y}{L}\right}\right).
       \]

       a. At each point on your grid, compute the fractional
          error of your series approximation to V. Display it as
          a colormap with imshow and a colorbar.

       b. Interpret this physically: where are the biggest
          fractional errors and why?
'''

import numpy as np

def compute_exact_potential(x, y, V0=1, L=np.pi):
    '''
    Computes the analytic solution for V(x, y).

    Parameters:
        x, y: np.ndarray
            Coordinates as meshgrid arrays.
        V0: float
            Boundary condition constant.
        L: float
            Width of the box in x.

    Returns:
        V_exact: np.ndarray
            Exact analytic solution for V(x, y).
    '''
    pi_over_L = np.pi / L
    numerator = np.sin(pi_over_L * x)
    denominator = np.sinh(pi_over_L * y)
    with np.errstate(divide='ignore', invalid='ignore'):
        V_exact = (2 * V0 / np.pi) * np.arctan(numerator / denominator)
    return V_exact

def compute_fractional_error(V_approx, V_exact):
    '''
    Computes fractional error between approximate and exact potential.

    Parameters:
        V_approx: np.ndarray
            Approximate potential from truncated series.
        V_exact: np.ndarray
            Exact analytic potential.

    Returns:
        frac_error: np.ndarray
            Element-wise fractional error.
    '''
    with np.errstate(divide='ignore', invalid='ignore'):
        error = np.abs(V_exact - V_approx)
        frac_error = np.where(np.abs(V_exact) > 1e-12, error / np.abs(V_exact), 0.0)
    return frac_error

