"""
Континуальный аргумент 2: key word arguments (именованные континуальные аругменты)

**kwargs -> {}
**dog
**cat
**_
"""

def build_info(**kwargs):
    """
    description
    """
    print("Type?:", type(kwargs))
    print("Values?:", kwargs)


def mutant(a,b, *args, **kwargs):
    pass


def main():
    """
    entry point
    """
    build_info(name="Vasya", last_name="Petrov", age=22, city="SPB")

main()