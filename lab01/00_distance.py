#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

# TODO здесь заполнение словаря

print(distances)

def distanc(sity1, sity2):
    x1, y1 = sites[sity1]
    x2, y2 = sites[sity2]
    return abs(x1 - x2) + abs(y1 - y2)



