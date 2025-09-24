#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть значение радиуса круга
radius = 42
PI = 3.1415926
# Выведите на консоль значение прощади этого круга с точностю до 4-х знаков после запятой
# подсказки:
#       формулу можно подсмотреть в интернете,
#       пи возьмите равным 3.1415926
#       точность указывается в функции round()

s = 3.1415926* radius**2
print(round(s,4))
# Далее, пусть есть координаты точки
point_1 = (23, 34)
# где 23 - координата х, 34 - координата у

# Если точка point лежит внутри того самого круга [центр в начале координат (0, 0), radius = 42],
# то выведите на консоль True, Или False, если точка лежит вовне круга.
# подсказки:
#       нужно определить расстояние от этой точки до начала координат (0, 0)
#       формула так же есть в интернете
#       квадратный корень - это возведение в степень 0.5
#       операции сравнения дают булевы константы True и False
if (((point_1[0] - 0)**2 + (point_1[1] - 0)**2) ** 0.5) <= radius**2:
    res = True
else:
    res = False
print (res)
# Аналогично для другой точки
point_2 = (30, 30)
# Если точка point_2 лежит внутри круга (radius = 42), то выведите на консоль True,
# Или False, если точка лежит вовне круга.
if (((point_2[0] - 0)**2 + (point_2[1] - 0)**2) ** 0.5) <= radius**2:
    res2 = True
else:
    res2 = False
print (res2)
# Пример вывода на консоль:
#
# 77777.7777
# False
# False


radius = 42
PI = 3.1415926
def calculateArea(radius):
    return PI * radius ** 2

def poinInCiecle(point, radius, center):
    x = point[0]
    y = point[1]
    x0 = center[0]
    y0 = center[1]
    distanse = ((x - x0)**2 + (y - y0)**2)**0.5
    return distanse <= radius**2


center = (0, 0)
point_1 = (23, 34)
point_2 = (30, 30)
area = PI * radius ** 2
print(round(area,4))
res1 = poinInCiecle(point_1, radius, center)
print(res1)
res2 = poinInCiecle(point_2, radius, center)
print(res2)

