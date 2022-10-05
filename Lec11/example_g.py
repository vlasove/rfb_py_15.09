# Решение задачи J
print(len(max(input().strip().split("р"))))

print(max([(len(elem), elem) for elem in input().strip().split("р")])[0])