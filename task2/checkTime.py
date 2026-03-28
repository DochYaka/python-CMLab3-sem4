from Logic.lagrange import lagrange
from Logic.newton import newton
from Logic.newton import divided_differences

import time
import numpy as np

def checkTime():
    x_points = [-2, 0, 1, 3, 5]
    y_points = [7, 6, 10, 9, 10]

    a, b = -5, 5
    x_vals = np.linspace(a, b, 500)

    # Ньютон
    start = time.time()

    coef = divided_differences(x_points, y_points)
    y_newton = [newton(x, x_points, coef) for x in x_vals]

    time_newton = time.time() - start

    # Лагранж
    start = time.time()

    y_lagrange = [lagrange(x, x_points, y_points) for x in x_vals]

    time_lagrange = time.time() - start


    print(f"Ньютон: {time_newton:.6f} сек")
    print(f"Лагранж: {time_lagrange:.6f} сек")