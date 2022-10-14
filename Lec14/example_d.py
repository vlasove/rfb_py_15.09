"""
пример игнорирования default value arg
"""

def add(x_arg = 1, y_arg = 0, z_arg =3):
    """
    description
    """
    return x_arg**2 + y_arg**3 + z_arg**4

def main():
    """
    entry point
    """
    print(add(x_arg=5, z_arg=5))

main()