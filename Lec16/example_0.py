"""
Пример анонимной функции
"""

def add(x_arg:int, y_arg:int):
    """
    Арифметическое сложение стеменных аргументов
    .........
    """
    return x_arg ** 3 + y_arg ** (2 + x_arg)


def main():
    """
    entry point
    """
    for i in range(1, 5):
        print(f"add({i}, {i+1}) is {add(i, i+1)}")
    print("value in add:", add)
    print("add type is:", type(add))

    variable_with_lambda = lambda x, y: x ** 3 + y ** (2 + x)
    print("value lambda:", variable_with_lambda)
    print("lambda type is:", type(variable_with_lambda))
    for i in range(1,5):
        print(variable_with_lambda(i, i + 1))

    

main()