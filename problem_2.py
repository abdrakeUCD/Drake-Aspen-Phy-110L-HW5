'''
Includes functions associated with problem 2, which reads:
    2. (Field lines.) Now switch to a 2D plot, showing the same
       part of the xy plane as in problem 1. Launch 50 uniformly
       spaced field lines from the y=0 boundary of the box.
       The field lines match the field you expect by taking
       minus the gradient of your potential in problem 1.
       State two things you observe about your field lines
       that (qualitatively) support this idea.
'''

import numpy as np


def compute_electric_field(x, y, N, V0=1, L=np.pi):
    '''
    Computes the electric field components -\nabla V from the potential function.

    Parameters:
        x, y: float or np.ndarray
            Coordinates where the field is evaluated
        N: int
            Number of Fourier terms
        V0: float
            Constant potential at y=0
        L: float
            Length of the box in x

    Returns:
        Ex, Ey: np.ndarray
            Electric field components array
    '''
    Ex = np.zeros_like(x)
    Ey = np.zeros_like(y)
    for n in range(1, N + 1, 2):  # odd n only
        coeff = 4 * V0 / (n * np.pi)
        alpha = n * np.pi / L
        Ex += coeff * alpha * np.cos(alpha * x) * np.exp(-alpha * y)
        Ey += -coeff * alpha * np.sin(alpha * x) * np.exp(-alpha * y)
    return -Ex, -Ey  # minus sign: E = -\nabla V


def step_rk2(starting_point: tuple[float, float],
             field_fn,
             step_size: float,
             propogation_coefficient: int = 1,
             equipotential: bool = False):
    '''
    Compute the next RK2 step using analytical field function.

    Parameters:
        starting_point: tuple
            The current (x, y) position.
        field_fn: function
            A callable that returns Ex, Ey at (x, y).
        step_size: float
            Step size of the RK2 integration.
        propogation_coefficient: int
            Direction of propagation (1 or -1).
        equipotential: bool
            If True, rotate the field vector 90 degrees.

    Returns:
        new_point: tuple
            The new (x, y) position.
    '''
    x, y = starting_point
    Ex1, Ey1 = field_fn(x, y)
    x_mid = x + 0.5 * step_size * Ex1
    y_mid = y + 0.5 * step_size * Ey1
    Ex2, Ey2 = field_fn(x_mid, y_mid)
    dx, dy = Ex2, Ey2
    ds_norm = step_size / np.sqrt(dx ** 2 + dy ** 2)
    dx = dx * ds_norm * propogation_coefficient
    dy = dy * ds_norm * propogation_coefficient
    if equipotential:
        dx, dy = -dy, dx
    return x + dx, y + dy


def trace_field_line(starting_point: tuple[float, float],
                     field_fn,
                     step_size: float,
                     max_steps: int,
                     bounds: tuple[float, float, float, float],
                     propogation_coefficient: int = 1):
    '''
    Trace a field line using RK2.

    Parameters:
        starting_point: tuple
            Initial (x, y) location.
        field_fn: callable
            A function that returns (Ex, Ey) at (x, y).
        step_size: float
            RK2 step size.
        max_steps: int
            Maximum number of integration steps.
        bounds: tuple
            (xmin, xmax, ymin, ymax) termination region.
        propogation_coefficient: int
            Direction (1 for with field, -1 against field).

    Returns:
        path_x, path_y: list
            Lists of x and y positions traced.
    '''
    path_x = [starting_point[0]]
    path_y = [starting_point[1]]
    point = starting_point
    for _ in range(max_steps):
        point = step_rk2(point, field_fn, step_size, propogation_coefficient)
        if not (bounds[0] <= point[0] <= bounds[1] and bounds[2] <= point[1] <= bounds[3]):
            break
        path_x.append(point[0])
        path_y.append(point[1])
    return path_x, path_y

