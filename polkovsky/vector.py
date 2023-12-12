class VectorError(Exception):
    def __init__(self):
        super().__init__('Один из объектов не является вектором')


class Vector:
    def __init__(self, *args):
        if len(args) not in [0, 1]:
            raise IndexError('Неверно задан вектор')

        if len(args) == 0:
            self.x, self.y, self.z = 0, 0, 0
        else:
            if type(args[0]) in [int, float]:
                self.x, self.y, self.z = args[0], args[0], args[0]
            elif type(args[0]) in [list, tuple]:
                if all([type(i) in [int, float] for i in args[0]]):
                    self.x, self.y, self.z = args[0][0], args[0][1], args[0][2]
                else:
                    raise IndexError('Неверно задан вектор')
            else:
                raise IndexError('Неверно задан вектор')

    def length(self) -> float:
        return (
                (self.x) ** 2 +
                (self.y) ** 2 +
                (self.z) ** 2
        ) ** 0.5

    def __abs__(self):
        return self.length()

    def __add__(self, other):
        if type(other) != Vector:
            raise VectorError

        return Vector([self.x + other.x, self.y + other.y, self.z + other.z])

    def __sub__(self, other):
        if type(other) != Vector:
            raise VectorError

        return Vector([self.x - other.x, self.y - other.y, self.z - other.z])

    def __neg__(self):
        return Vector([-self.x, -self.y, -self.z])

    def __mul__(self, other):
        if type(other) not in [Vector, float, int]:
            raise VectorError

        if type(other) in [int, float]:
            return Vector([self.x * other, self.y * other, self.z * other])
        else:
            return self.x * other.x + self.y * other.y + self.z * other.z

    def __xor__(self, other):
        if type(other) != Vector:
            raise VectorError

        x = self.y * other.z - self.z * other.y
        y = - (self.x * other.z - self.z * other.x)
        z = self.x * other.y - self.y * other.x

        return Vector([x, y, z])

    @staticmethod
    def triple_product(a, b, c):
        if [type(a), type(b), type(c)] != [Vector, Vector, Vector]:
            raise VectorError
        return a.x * (b.y * c.z - b.z * c.y) - (a.y * (b.x * c.z - b.z * c.x)) + a.z * (b.x * c.y - b.y * c.x)

    def __or__(self, other):
        if type(other) != Vector:
            raise VectorError
        return self.x / other.x == self.y / other.y == self.z / other.z

    @staticmethod
    def are_complanar(a, b, c):
        if [type(a), type(b), type(c)] != [Vector, Vector, Vector]:
            raise VectorError
        return a.x * (b.y * c.z - b.z * c.y) - (a.y * (b.x * c.z - b.z * c.x)) + a.z * (b.x * c.y - b.y * c.x) == 0

    def __str__(self):
        return f'Vector: x={self.x} y={self.y} z={self.z}'


if __name__ == '__main__':
    v1 = Vector()
    v2 = Vector(1)
    v3 = Vector([5, 1, -1.5])
    print(v3)
    print(v3 + v2)
