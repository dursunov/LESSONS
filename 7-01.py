class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return "\n".join("\t".join([str(el) for el in line]) for line in self.data)

    def __add__(self, other):
        m = [[int(self.data[line][el]) + int(other.data[line][el]) for el in range(len(self.data[line]))]
             for line in range(len(self.data))]
        print(Matrix(m))


m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m1 = Matrix(m1)
m2 = Matrix(m2)

nm = m1 + m2
