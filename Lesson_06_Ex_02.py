class Road:
    def mascal(self, _length, _width):
        sq_met = 25     # масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см
        dep = 5         # число см толщины полотна
        return (str(int(_length * _width * sq_met * dep / 1000))+" тонн")

alWahda = Road()
print(alWahda.mascal(5000, 20))
