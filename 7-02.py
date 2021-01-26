from abc import abstractmethod, ABC


class Clothers(ABC):
    def __init__(self, p):
        self.p = p
    @property
    @abstractmethod
    def rashod(self): pass
    def __add__(self, other): return self.rashod + other.rashod


class Coat(Clothers):
    @property
    def rashod(self): return f'for  {self.p} size, u will spend {round(self.p / 6.5 + 0.5)}'

class Cost(Clothers):
    def rashod(self): return f'for height  {self.p} , u will spend {round(2 * self.p + 0.3)}'


coat = Coat(35)
cost = Cost(160)
print(coat.rashod)
print(cost.rashod())
