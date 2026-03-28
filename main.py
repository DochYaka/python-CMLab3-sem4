from task1.task1 import graph_Interpolation_Polynomial
from matrixSolution import gauss_with_pivot

# Данные
x_points = [-2, 0, 1, 3, 5]
y_points = [7, 6, 10, 9, 10]


# Задание 1

# Задание 1.1 | по пяти значениям функции определить коэффициенты 
#интерполяционного многочлена с помощью решения СЛАУ.
A = [ [1, -2, 4, -8, 16],
    [1,  0, 0,  0,  0],
    [1,  1, 1,  1,  1],
    [1,  3, 9, 27, 81],
    [1,  5,25,125,625] ]
b = [7, 6, 10, 9, 10]

a = gauss_with_pivot(A, b)

graph_Interpolation_Polynomial(x_points, y_points, a)
