class Cell:
    def __init__(self, nums):
        self.nums = int(nums)

    def make_order(self, rows):
        return "\n".join(["*" * rows for _ in range(self.nums // rows)]) + "\n" + "*" * (self.nums % rows)

    def __str__(self):
        return f"{self.nums}"

    def __add__(self, other):
        print("summ=", end="")
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print("subtraction = ", end="")
        return (Cell(self.nums - other.nums))

    def __mul__(self, other):
        print("multiplication = ", end="")
        return (Cell(self.nums * other.nums))

    def __floordiv__(self, other):
        print("tselaya chast' ot deleniya = ", end="")
        return (Cell(self.nums // other.nums))


c1 = Cell(159)
c2 = Cell(956)

print(c1 + c2)
print(c1 - c2)
print(c1 * c2)
print(c1 // c2)
print(c1.make_order(12))
