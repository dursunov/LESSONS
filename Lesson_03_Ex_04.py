# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

# Первый вариант
def my_func(x, y):
    while y >= 0:
        y = int(input(
            "Вы ввели число больше или равно нулю, но по условию задачи степень должна быть отрицательной. Введите положительную степень числа X повторно:   "))
    return x ** y


# Второй вариант
def my_func2(x, y):
    while y >= 0:
        y = int(input("По условию задачи степень должна быть отрицательной. Введите положительную степень числа X:  "))
    d = 1
    for el in range(abs(y)):
        d *= x
    return 1 / d

# print(my_func(2,-2))
# print(my_func(2,2))
# print(my_func2(2,-2))
# print(my_func2(2,2))