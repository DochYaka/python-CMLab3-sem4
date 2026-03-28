from Logic.lagrange import lagrange
from Logic.newton import newton
from Logic.matrixSolution import gauss_with_pivot
import matplotlib.pyplot as plt
import numpy as np

# Задание 1.1 | по пяти значениям функции определить коэффициенты 
#интерполяционного многочлена с помощью решения СЛАУ.

def poly(x, a):
    return sum(a[i] * x**i for i in range(len(a)))

def graph_Interpolation_Polynomial(x_points, y_points, A, b):
    a = gauss_with_pivot(A, b)
    x_vals = np.linspace(-3, 6, 100)
    y_vals = [poly(x, a) for x in x_vals]

    plt.plot(x_vals, y_vals, label="P(x)")

    plt.scatter(x_points, y_points, color='red', label="Исходные точки")

    plt.legend()
    plt.grid()
    plt.title("Интерполяционный многочлен")
    plt.show()


# Задание 1.2 | построение графика интерполяционного многочлена 
# в форме Лагранжа по заданным точкам.

def graph_Interpolation_Polynomial_Lagrange_Form(x_points, y_points):
    x_vals = np.linspace(-3, 6, 100)
    y_vals_lagrange = [lagrange(x, x_points, y_points) for x in x_vals]

    plt.plot(x_vals, y_vals_lagrange, label="Лагранж")

    plt.scatter(x_points, y_points, color='red', label="Исходные точки")

    plt.legend()
    plt.grid()
    plt.title("Интерполяционный многочлен в форме Лагранжа")
    plt.show()

# Задание 1.3 | построение графика интерполяционного многочлена 
# в форме Лагранжа по заданным точкам.

def graph_Interpolation_Polynomial_Newton_Form(x_points, y_points):
    x_vals = np.linspace(-3, 6, 100)
    y_vals_newton = [newton(x, x_points, y_points) for x in x_vals]
    
    plt.plot(x_vals, y_vals_newton, label="Ньютон")

    plt.scatter(x_points, y_points, color='red', label="Исходные точки")

    plt.legend()
    plt.grid()
    plt.title("Интерполяционный многочлен в форме Ньютона")
    plt.show()