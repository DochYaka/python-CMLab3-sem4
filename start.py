from task1 import graphs1
from task2 import graphs2
from task2 import checkTime

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

    graphs1.graph_Interpolation_Polynomial(x_points, y_points, A, b)

    # Задание 1.2 | построение графика интерполяционного многочлена 
    # в форме Лагранжа по заданным точкам.
    graphs1.graph_Interpolation_Polynomial_Lagrange_Form(x_points, y_points)

    # Задание 1.3 | построение графика интерполяционного многочлена 
    # в форме Ньютона по заданным точкам.
    graphs1.graph_Interpolation_Polynomial_Newton_Form(x_points, y_points)


# Задание 2
def task2():
    # # Данные
    # n = int(input("Количество точек: "))
    # x0 = float(input("Начальное значение x: "))
    # h = float(input("Шаг: "))

    # # Задание 2.1 | построение графиков по трём различным функциям в форме Лагранжа.
    # graphs2.graph_True(n, x0, h)
    # graphs2.graph_Interpolation_Polynomial_Lagrange_Form(n, x0, h)
    
    # Задание 2.2 | сравнение графиков интерполяционного многочлена
    # в форме Лагранжа с увеличением кол-ва точек.
    graphs2.graph_Interpolation_Polynomial_Lagrange_Form_FixInterval()

    # # Задание 2.3 | сравнение скорости выполнения методов Ньютона и Лагранжа.
    # checkTime.checkTime()

    # Задание 2.4 | сравнение результатов способов при большом кол-ве точек (более 10)
    graphs2.graph_Interpolation_Polynomial_Newton_Form_FixInterval()



    
