class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, object):
        self.name = object.name
        self.surname = object.surname
        self.position = object.position
        self.income = object._income

    def get_full_name(self):
        print(self.name, self.surname)

    def get_total_income(self):
        print(self.income["wage"] + self.income["bonus"])


a = Worker("Жорик", "Бубликов", "Директор", {"wage": 1000000, "bonus": 100000})  # создаём объект класса Worker
b = Position(a)  # создаём объект дочернего от Worker класса Position, используя в кач-ве аргумента объект класса Worker
b.get_full_name()
b.get_total_income()
