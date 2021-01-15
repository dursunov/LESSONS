class Car:
    def __init__(self, speed, color, name, s_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.s_police = s_police
    def go(self): # которые должны сообщать, что машина поехала, остановилась, повернула (куда)
        print("Ваша машина начала двигаться")
    def stop(self):
        print("Ваша машина остановилась")
    def direction(self, dir):
        print("Ваша машина повернула", dir)

    def show_speed(self):
        print("Ваша текущая скорость: ", self.speed)

class TownCar(Car):
    def __init__(self, speed, color, name, s_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.s_police = 0
    def show_speed(self):
        if self.speed >=60:
            print("Ваша скорость - ",self.speed,"км/ч")
            print("Вы превышаете скорость")
class SportCar(Car):
    pass
class WorkCar(Car):
    def __init__(self, speed, color, name, s_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.s_police = 0
    def show_speed(self):
        if self.speed >=40:
            print("Ваша скорость - ",self.speed,"км/ч")
            print("Вы превышаете скорость")
class PoliceCar(Car):
    pass


print("☺"*15)
basic_car = Car(100,"RED", "Mitsubishi Paj0ero", 0)
basic_car.go()
basic_car.direction("налево")
basic_car.show_speed()
print(basic_car.speed)
print(basic_car.name)
print(basic_car.color)
print(basic_car.s_police)

print("☺"*15)
tonwcar1 = TownCar(100,"RED", "Mitsubishi Paj0ero", 0)
tonwcar1.show_speed()
tonwcar1.direction("направо")
print(tonwcar1.speed)
print(tonwcar1.name)
print(tonwcar1.color)
print(tonwcar1.s_police)

print("☺"*15)
workcar1 = WorkCar(41, "BLUE", "VAG", 0)
workcar1.show_speed()
print("☺"*15)

policecar1 =  PoliceCar("35", "PINK", "LADA", 1)
policecar1.show_speed()
policecar1.direction("направо")
print("☺"*15)
spoca = SportCar("110", "BLACK", "Fa_Car", 0)
spoca.direction("на север")
spoca.show_speed()
