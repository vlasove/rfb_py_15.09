"""
Простейший возврат
"""

def add(a, b):
    return a**2 + b**3

res = add(10, 9)
print("Result outside function:", res)

#########################
answer = add(2, -4) + add(1, 1) // 2 + add(2,3) ** 2
print(f"Answer:{answer}")

"""
Чуть более подробно про возврат значений из функций
1) Функции в Python всегда что-то возвращают
2.1) Если в теле функции присутствует `return val` - функция будет пытаться вернуть
val
2.2) Иначе если в теле функции явно не присутствует return / ИЛИ присутствует пустой `return` - 
по умолчанию возвращается None
"""
def sub(a, b):
    """
    Арифметическая разность a - b
    """
    res = a - b 
    print(res)
    return

sub_result = sub(10, 2)
if sub_result is None: # Проверка на None
    print("sub(10,2) is:", sub_result)
else:
    print("second move")



nums = [10, 2, 3]
nums.sort()
print(nums)


"""
Множественный возврат (возврат нескольких значений) - его в Python нет
"""


def get_sides():
    """
    Возвращает стороны треугольника
    """
    return (10, 2, 7)


a, b, c = get_sides()
print("a is:", a)
print("b is:", b)
print("c is:", c)
