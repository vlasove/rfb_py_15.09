# Решение задачи D

birthdays = {}

n = int(input().strip()) # Количество друзей для добавления в книгу
for _ in range(n):
    name, _, month = input().strip().split() # "Вася 10 май" -> ["Вася", "10", "май"]
    if month in birthdays.keys():
        birthdays[month].append(name)
    else:
        birthdays[month] = [name]

m = int(input().strip()) # Количество запросов к книге
for _ in range(m):
    month = input().strip()
    if month in birthdays.keys():
        print(" ".join(sorted(birthdays[month])))
    else:
        print()