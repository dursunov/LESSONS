# Создайте собственный класс-исключение,
# обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.


class DBZ:
    def __init__(self, d, dd):
        self.d = d
        self.dd = dd

    @staticmethod
    def divide_by_null(d, dd):
        try:
            return (d / dd)
        except:
            return (f"#DIV/0")


div = DBZ(10, 100)
print(DBZ.divide_by_null(1000000000000000000, 0))


print(DBZ.divide_by_null(1000,1e+400))

print(DBZ.divide_by_null(10,1e-400))
print(div.divide_by_null(100, 0))

print(DBZ.divide_by_null(1e+90000,1e+10))
print(DBZ.divide_by_null(1e+4000,1e+90000))