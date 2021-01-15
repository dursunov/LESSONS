class Stationery():
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print("Отрисовка запуска")


class Pencil(Stationery):
    def draw(self):
        print("Запуск остановки отрисовки")


class Handle(Stationery):
    def draw(self):
        print("Остановка отрисовки запуска отрисовки остановки")


s = Stationery("Карандаш")
print(s.title)
s.draw()

p = Pen("Ручка")
print(p.title)
p.draw()
z = Pencil("Карандаш")
print(z.title)
z.draw()
o = Handle("Маркер")
print(o.title)
o.draw()
