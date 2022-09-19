# Решение задачи M
n = int(input())

for i in range(-n, n + 1, 1): # (-2, 3, 1) -> -2, -1, 0, 1, 2
    squared = i ** 2
    print(f"Квадрат числа {i} равен {squared}")