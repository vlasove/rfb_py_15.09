"""
example_b:
    Тщетные попытки достучаться до элементов
    модуля example_a
"""


# 1. Способ с разделяющей областью пространств имен
import example_a as ex

# import math
# import sys
# import os
# import datetime
# import time
# import json


MAX_ATTEMPTS = 12
add = lambda x,y : x + y

print("Max attempts here:", MAX_ATTEMPTS)
print("Add here:", add(2,3))

print(ex.MAX_ATTEMPTS)
print(ex.add(10, 12))

# print(math.pi)
# print(math.sqrt(12))


# import example_a as ex # импортирование с РАЗДЕЛЯЮЩИЕЙ ОБЛАСТЬЮ


# MAX_ATTEMPTS = 999999
# add = lambda x,y : x ** 2 - y ** 2

# # print(ex, dir(ex)) - ex - тоже объект с методами и атрибутами
# print(ex.MAX_ATTEMPTS)
# print(ex.add(2, 3))


# print(MAX_ATTEMPTS)
# print(add(2,3))


