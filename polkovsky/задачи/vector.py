'''Разработать класс Vector, в основе которого лежит упорядоченный набор трёх целых чисел.
Предусмотреть для этого класса следующие атрибуты и методы:
1) атрибуты x, y, z — координаты вектора;
2) конструктор init, который может вызываться с различными параметрами: либо список/кортеж из трёх чисел, либо одно целое число
(в таком случае все координаты вектора будут равны этому числу), либо вообще без параметров
(и тогда все координаты создаваемого вектора будут равны нулю);
3) метод length — длина вектора; аналогичный код прописать и для метода abs, перегрузив стандартную функцию abs ;
4) операции сложения и вычитания векторов: использовать для этого перегрузку операторов + и - ;
5) дополнительно перегрузить для вектора унарный минус, действие которого будет равносильно умножению вектора на минус единицу;
6) операции умножения вектора на число и скалярного произведения векторов: использовать для этого оператор * ;
7) операцию векторного произведения, перегрузив оператор ^ ;
8) статистический метод Vector.triple_product(a, b, c), вычисляющий смешанное произведение векторов a, b и c;
9) оператор | (pipe), возвращающий True, если векторы коллинеарны, и False в противном случае;
10) статический метод Vector.are_complanar(a, b, c), возвращающий True, если векторы a, b и c компланарны, и False в противном случае.
Если что — по некоторым моментам подскажу на ближайшем занятии.
Шпаргалка по перегрузке операторов в классах приложена ниже (см. стр. 2).'''


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
        return self^other == Vector([0,0,0])



    @staticmethod
    def are_complanar(a, b, c):
        if [type(a), type(b), type(c)] != [Vector, Vector, Vector]:
            raise VectorError
        return a.x * (b.y * c.z - b.z * c.y) - (a.y * (b.x * c.z - b.z * c.x)) + a.z * (b.x * c.y - b.y * c.x) == 0

    def __str__(self):
        return f'Vector: x={self.x} y={self.y} z={self.z}'

    def __eq__(self, other):
        return self.x - other.x == self.y - other.y == self.z - other.z

if __name__ == '__main__':
    v1 = Vector([1,1,1])
    v2 = Vector([2,2,2])
    v3 = Vector([3,4,5])
    v0 = Vector([0,0,0])
    #v4 = Vector([])
    print(v3|v1)
    print(v1| v2)
    print(v1|v0)
