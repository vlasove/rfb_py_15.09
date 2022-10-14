"""
Аргументы со значением по умолчанию (Default Values Args)
"""

def add(a = 0, b = 1):
    print("a is:", a)
    print("b is:", b)
    return a ** 2 + b ** 3

def shift(shifting, x_arg = 0.0,  y_arg = 0.0):
    """
    shifting - абсолютное значение сдвига (обязательный параметр)
    x_arg, y_arg - начальные координаты до сдвига (необязательные параметры, по умолчанию 0.0)

    возвращает кортеж (x_arg + shift, y_arg + shift)
    """
    return (x_arg + shifting, y_arg + shifting)

shift(10)

def main():
    """
    входная точка в приложение
    """
    print(add())
    print(add(3))
    print(add(1,2))
    print(add(b = 10))
    # print(add(1,2,3))
    
    x, y = shift(5, 12.5, 13.5)
    print(f"X:{x}, Y:{y}")

main()