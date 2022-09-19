# Решение задачи О
n = int(input())

summ = 0

for i in range(n):
    numeric = int(input())
    if i % 2 == 0:
        summ += numeric
    else:
        summ -= numeric

print(summ)

# 10 - 12 + 33 - 14 + 45 - ....
# 0    1    2    3    4