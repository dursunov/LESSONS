class Error:
    def __init__(self, *args):
        self.my_list = []

    def my_input(self):

        while True:
            try:
                val = int(input('набиваем список (Enter), для завершения - пустое поле - '))
                self.my_list.append(val)
                print(f'Список  - {self.my_list} \n ')
            except:
                print(f"Недопустимое значение - строка и булево")
                y_or_n = input(f'One more time?  Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.my_input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'quit ☺'
                else:
                    return f'exit ☺'


try_except = Error(1)
print(try_except.my_input())