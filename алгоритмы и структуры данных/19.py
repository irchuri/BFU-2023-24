class Point:
    def __init__(self, x: (int, float), y: (int, float)):
        '''
        Задание точки по 2 координатам
        TODO: Передавать кортеж, список
        '''
        if not isinstance(x, (int, float)):
            raise TypeError('x должен быть объектом типа float или int')
        if not isinstance(y, (int, float)):
            raise TypeError('y должен быть объектом типа float или int')

        self.x, self.y = x, y

    def __eq__(self, other):
        '''
        Проверка точек на равенство друг с другом или с кортежем или со списком
        Point == Point
        Point == [1,1]
        Point == (1,1)
        '''
        if isinstance(other, Point):
            return (self.x, self.y) == (other.x, other.y)
        elif isinstance(other, (tuple, list)):
            if len(other) != 2:
                raise IndexError('Длина списка или кортежа должна быть равна 2')
            return (self.x, self.y) == (other[0], other[1])
        else:
            raise NotImplementedError(f'Невозможно сравнить Point и {type(other)}')

    def __ne__(self, other):
        '''
        Проверка точек на неравенство друг с другом или с кортежем или со списком
        Point == Point
        Point == [1,1]
        Point == (1,1)
        '''
        return not self == other

    def __str__(self):
        return f'Point(x={self.x}, y={self.y})'


class TiLoxError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Line:
    def __init__(self, A: Point, B: Point):
        if A == B:
            raise ValueError('Точки задания прямой не должны быть равны')
        x1 = A.x
        y1 = A.y
        x2 = B.x
        y2 = B.y
        self.A = y2 - y1
        self.B = -(x2 - x1)
        self.C = y1 * (x2 - x1) - x1 * (y2 - y1)

    def __xor__(self, other):
        if isinstance(other, (Line, Segment)):
            A1, B1, C1 = self.A, self.B, self.C
            A2, B2, C2 = other.A, other.B, other.C

            try:
                x = (C1 / B1 - C2 / B2) / (A2 / B2 - A1 / B1)
                y = -C1 / B1 - A1 * x / B1
                if isinstance(other, (Segment,)):
                    left_x = min(other.end1.x, other.end2.x)
                    right_x = max(other.end1.x, other.end2.x)
                    upper_y = max(other.end1.y, other.end2.y)
                    lower_y = min(other.end1.y, other.end2.y)
                    if (left_x <= x <= right_x) and (lower_y <= y <= upper_y):
                        return Point(x, y)
                    else:
                        bimbimbambam = 0 / 0
                if isinstance(other, (Line,)):
                    return Point(x, y)
            except ZeroDivisionError:
                raise TiLoxError('Объекты не имеют общих точек или имеют бесконечное множество таковых.')
        if isinstance(other, (Circle,)):
            return other ^ self

        raise NotImplementedError(f'Не реализовано пересечение Line и {type(other)}')


class Segment:
    def __init__(self, A: Point, B: Point):
        if A == B:
            raise ValueError('Точки задания отрезка не должны быть равны')
        x1 = A.x
        y1 = A.y
        x2 = B.x
        y2 = B.y
        self.A = y2 - y1
        self.B = -(x2 - x1)
        self.C = y1 * (x2 - x1) - x1 * (y2 - y1)
        self.end1 = A
        self.end2 = B
        self.parent_line = Line(A, B)

    def length(self) -> float:
        return ((self.end1.x - self.end2.x) ** 2 + (self.end1.y - self.end2.y) ** 2) ** 0.5

    def point_on_me(self, point):
        # print(f'DEBUG: sum: {Segment(self.end1, point).length() + Segment(point, self.end2).length()}')
        # print(f'DEBUG: len: {self.length()}')
        # Проблема компов - неточность вычислений
        return abs(
            (
                    Segment(self.end1, point).length() +
                    Segment(point, self.end2).length()
            ) - self.length()
        ) < 10 ** -13

    def __xor__(self, other):
        if isinstance(other, (Line,)):
            return other ^ self
        if isinstance(other, (Segment,)):                                                                                    # Я инженер
            potential_intersection_point = self.parent_line ^ other.parent_line                                              # Я не #бу как оно работает
            if self.point_on_me(potential_intersection_point) and other.point_on_me(potential_intersection_point):           # Если тебе интересно, как это работает, смотри чертежи
                return potential_intersection_point                                                                          # Лично мне - по#бать'''
            raise TiLoxError('Объекты не имеют общих точек')
        if isinstance(other, (Circle,)):
            return other ^ self
        raise NotImplementedError(f'Не реализовано пересечение Segment и {type(other)}')


class Circle:
    def __init__(self, A: Point, B: Point, C: Point):
        x1, y1 = A.x, A.y
        x2, y2 = B.x, B.y
        x3, y3 = C.x, C.y

        D = 2 * (x1 - x2)
        E = 2 * (y1 - y2)
        F = x1 ** 2 - x2 ** 2 + y1 ** 2 - y2 ** 2

        G = 2 * (x2 - x3)
        H = 2 * (y2 - y3)
        I = x2 ** 2 - x3 ** 2 + y2 ** 2 - y3 ** 2

        # Находим центр (h, k)
        h = (F * H - I * E) / (D * H - E * G)
        k = (D * I - G * F) / (D * H - E * G)

        # Находим радиус r
        r = ((x1 - h) ** 2 + (y1 - k) ** 2) ** 0.5

        self.center = Point(h, k)
        self.radius = r

    def __xor__(self, other):
        if isinstance(other, (Line,)):
            # ax^2 + bx + c = 0
            A = other.A
            B = other.B
            C = other.C
            x1 = self.center.x
            y1 = self.center.y
            R = self.radius

            a = 1 + (A / B) ** 2
            b = (-2 * x1 + (2 * A / B) * (C / B + y1))
            c = (x1 ** 2 + (C / B + y1) ** 2 - R ** 2)

            D = b ** 2 - 4 * a * c
            if D < 0:
                raise TiLoxError('Объекты не имеют общих точек')
            if D == 0:
                x = -b / (2 * a)
                y = (-C - A * x) / B
                return (Point(x, y),)
            else:
                x1 = (-b + D ** 0.5) / (2 * a)
                x2 = (-b - D ** 0.5) / (2 * a)
                y1 = (-C - A * x1) / B
                y2 = (-C - A * x2) / B
                return Point(x1, y1), Point(x2, y2)
        if isinstance(other, (Segment,)):
            result = self ^ other.parent_line
            result = [i for i in result if other.point_on_me(i)]
            if result:
                return tuple(result)
            raise TiLoxError('Объекты не имеют общих точек')

        if isinstance(other, Circle):
            x1 = self.center.x
            x2 = other.center.x
            y1 = self.center.y
            y2 = other.center.y
            R1 = self.radius
            R2 = other.radius

            # Расстояние между центрами окружностей
            d = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

            # Проверка на пересечение окружностей
            if d > R1 + R2 or d < abs(R1 - R2):
                raise TiLoxError('Объекты не имеют общих точек')

            # Вычисление координат точек пересечения
            a = (R1 ** 2 - R2 ** 2 + d ** 2) / (2 * d)
            h = (R1 ** 2 - a ** 2) ** 0.5
            x3 = x1 + a * (x2 - x1) / d
            y3 = y1 + a * (y2 - y1) / d

            intersection_point1 = (x3 + h * (y2 - y1) / d, y3 - h * (x2 - x1) / d)
            intersection_point2 = (x3 - h * (y2 - y1) / d, y3 + h * (x2 - x1) / d)
            if intersection_point1 == intersection_point2:
                return (Point(*intersection_point1), )
            else:
                return Point(*intersection_point1), Point(*intersection_point2)