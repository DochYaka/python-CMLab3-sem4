from task1 import graphs

def start(choice):
    if (choice == "task1" or choice == "1"):
        task1()
    else:
        task2()


# Задание 1
def task1():
    # Данные
    x_points = [-2, 0, 1, 3, 5]
    y_points = [7, 6, 10, 9, 10]
    
    # Задание 1.1 | по пяти значениям функции определить коэффициенты 
    #интерполяционного многочлена с помощью решения СЛАУ.
    A = [ [1, -2, 4, -8, 16],
        [1,  0, 0,  0,  0],
        [1,  1, 1,  1,  1],
        [1,  3, 9, 27, 81],
        [1,  5,25,125,625] ]
    b = [7, 6, 10, 9, 10]

    graphs.graph_Interpolation_Polynomial(x_points, y_points, A, b)

    # Задание 1.2 | построение графика интерполяционного многочлена 
    # в форме Лагранжа по заданным точкам.
    graphs.graph_Interpolation_Polynomial_Lagrange_Form(x_points, y_points)

    # Задание 1.3 | построение графика интерполяционного многочлена 
    # в форме Ньютона по заданным точкам.
    graphs.graph_Interpolation_Polynomial_Newton_Form(x_points, y_points)


# Задание 2
def task2():
   return 0
    
