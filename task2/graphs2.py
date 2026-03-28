from Logic.lagrange import lagrange
from Logic.newton import newton
from Logic.newton import divided_differences

import matplotlib.pyplot as plt
import numpy as np

# Задание 2.1 | построение графиков по трём различным функциям в форме Лагранжа
# def f(x):
#     return x**2

def f(x):
    return np.sin(x)

# def f(x):
#     return x**3 - 2*x + 1

def graph_True(n, x0, h):
    x_points = [x0 + i*h for i in range(n)]
    y_points = [f(x) for x in x_points]

    x_vals = np.linspace(min(x_points)-1, max(x_points)+1, 200)
    y_vals = [f(x) for x in x_vals]

    plt.plot(x_vals, y_vals, label="f(x)")

    plt.scatter(x_points, y_points, color='red', label="Исходные точки")

    plt.legend()
    plt.grid()
    plt.title("Исходная функция")
    plt.show()

def graph_Interpolation_Polynomial_Lagrange_Form(n, x0, h):
    x_points = [x0 + i*h for i in range(n)]
    y_points = [f(x) for x in x_points]

    x_vals = np.linspace(min(x_points)-1, max(x_points)+1, 200)
    y_vals = [lagrange(x, x_points, y_points) for x in x_vals]

    plt.plot(x_vals, y_vals, label="Интерполяция (Лагранж)")

    plt.scatter(x_points, y_points, color='red', label="Исходные точки")

    plt.legend()
    plt.grid()
    plt.title("Интерполяция (Лагранж)")
    plt.show()


# Задание 2.2 | сравнение графиков интерполяционного многочлена
# в форме Лагранжа с увеличением кол-ва точек.
def graph_Interpolation_Polynomial_Lagrange_Form_FixInterval():
    a, b = -5, 5
    x_vals = np.linspace(a, b, 500)

    for n in [5, 15, 20]:
        x_points = np.linspace(a, b, n)
        y_points = [f(x) for x in x_points]

        y_vals = [lagrange(x, x_points, y_points) for x in x_vals]

        plt.plot(x_vals, y_vals, label=f"n={n}")

        plt.scatter(x_points, y_points, color='red', label="Исходные точки")

    plt.grid()
    plt.legend()
    plt.title("Сравнение графиков")
    plt.show()

# Задание 2.4 | сравнение результатов способов при большом кол-ве точек (более 10)
def graph_Interpolation_Polynomial_Newton_Form_FixInterval():
    a, b = -5, 5
    x_vals = np.linspace(a, b, 500)

    for n in [5, 15, 20]:
        x_points = np.linspace(a, b, n)
        y_points = [f(x) for x in x_points]

        coef = divided_differences(x_points, y_points)

        y_vals = [newton(x, x_points, coef) for x in x_vals]

        plt.plot(x_vals, y_vals, label=f"n={n}")

    plt.scatter(x_points, y_points, color='red', label="Исходные точки")

    plt.grid()
    plt.legend()
    plt.title("Интерполяционный многочлен в форме Ньютона")
    plt.show()

