class Vector:
    def __init__(self, x0=None, y0=None, z0=None):
        if (x0 is None) and (y0 is None) and (z0 is None):
            self.x, self.y, self.z = 0, 0, 0
        elif x0 is not None:
            if type(x0) == list or type(x0) == tuple:
                self.x, self.y, self.z = x0[0], y0[1], z0[2]

    @staticmethod
    def vector_product(a, b):
        x3 = a.x * b.x - a.y * b.y
        y3 = a.y * b.y - a.z * b.z
        z3 = a.z * b.z + a.x * b.x
        return Vector(x3, y3, z3)


v1 = Vector(1, 2, 3)
print(v1.x)
