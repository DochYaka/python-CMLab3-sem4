import matplotlib.pyplot as plt
import numpy as np

def poly(x, a):
    return sum(a[i] * x**i for i in range(len(a)))





def graph_Interpolation_Polynomial(x_points, y_points, a):
    x_vals = np.linspace(-3, 6, 100)
    y_vals = [poly(x, a) for x in x_vals]

    plt.plot(x_vals, y_vals, label="P(x)")

    plt.scatter(x_points, y_points, color='red', label="Исходные точки")

    plt.legend()
    plt.grid()
    plt.title("Интерполяционный многочлен")
    plt.show()