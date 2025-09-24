#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
#garden_set = set(garden)
#meadow_set = set(meadow)
# выведите на консоль все виды цветов

#print (garden_set)
#print(meadow_set)
# выведите на консоль те, которые растут и там и там
#print(garden_set & meadow_set)

# выведите на консоль те, которые растут в саду, но не растут на лугу
#print(garden_set - meadow_set)
# выведите на консоль те, которые растут на лугу, но не растут в саду
#print(meadow_set - garden_set)

def flowersSet():
    garden_set = set(garden)
    meadow_set = set(meadow)
    print(garden_set)
    print(meadow_set)
    print("Цветы, которые растут и там и там", garden_set & meadow_set)
    print("Цветы, которые растут в саду, но не растут на лугу", garden_set - meadow_set)
    print("Цыеты, которые растут на лугу, но не ратут в саду", meadow_set - garden_set)
    return ""