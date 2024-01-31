from __future__ import annotations
from typing import Optional, Callable, Any
import matplotlib.pyplot as plt
from random import randint as rint, random as rand



def get_points() -> Any:
    try:
        num_points = int(input("Введите количество точек: "))
    except ValueError:
        print("Ошибка ввода! Введите корректное целое число.")
        return []

    pointsList = []
    for i in range(num_points):
        try:
            x = float(input(f"Введите координату X для точки {i + 1}: "))
            y = float(input(f"Введите координату Y для точки {i + 1}: "))
        except ValueError:
            print("Ошибка ввода! Введите корректные координаты.")
            return []

        pointsList.append([x, y])

    return pointsList


def orientation(p1, p2, p3):
    x1, y1, x2, y2, x3, y3 = *p1, *p2, *p3
    d = (y3 - y2) * (x2 - x1) - (y2 - y1) * (x3 - x2)
    if d > 0:
        return 1
    elif d < 0:
        return -1
    else:
        return 0


def dist(p1, p2):
    x1, y1, x2, y2 = *p1, *p2
    return ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5


def gift_wrapping(points: list):
    on_hull = min(points)
    hull = []
    while True:
        hull.append(on_hull)
        next_point = points[0]
        for point in points:
            o = orientation(on_hull, next_point, point)
            if next_point == on_hull or o == 1 or (o == 0 and dist(on_hull, point) > dist(on_hull, next_point)):
                next_point = point
        on_hull = next_point
        if on_hull == hull[0]:
            break
    return hull


# points_list = get_points() #True если функция что-то вернула

# if points_list:
#     print("Введённые точки:")
#     for i in range(len(points_list)):
#         point = points_list[i]
#         print(f"Точка {i + 1}: ({point[0]}, {point[1]})")


if __name__ == "__main__":
    points_list = [[rint(-100, 100)+rand(), rint(-100, 100)+rand()] for _ in range(rint(4, 50))]
    hull = gift_wrapping(points_list)
    print(hull)

    fig, ax = plt.subplots()

    ax.set_xlim(-150, 150)
    ax.set_ylim(-150, 150)
    ax.set_aspect('equal', adjustable='box')

    plt.scatter([i[0] for i in points_list], [i[1] for i in points_list], color='b', marker='.')
    hull_obj = plt.Polygon(hull, edgecolor='r', facecolor='none')

    ax.add_patch(hull_obj)
    plt.draw()
    plt.title('Convex hull for points')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.grid(True)
    plt.show()
