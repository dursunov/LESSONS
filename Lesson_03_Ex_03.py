# Реализовать функцию my_func(), которая
# принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.

def my_func(x, y, z):
    return (max(x, y, z) + max(x, y))

print(my_func(1,2,3))
print(my_func(4,5,6))
print(my_func(7,8,9))
