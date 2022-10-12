# На вход программе поступает n - информация про друзей
# Про каждого друга известно "Имя Месяц" (где имя - имя друга, месяц - это месяц когда он родился)
# Задача - сохранить друзей удобным для обработки образом

# birthdays = {}
# months = ["янв" , "фев", "мар"]
# birthdays = birthdays.fromkeys(months, [])
# print(birthdays)
# С прединициализированным словарем
birthdays = {
    "янв" : [],
    "фев" : [],
    "мар" : [],
    "апр" : [],
    "май" : [],
    "июн" : [],
    "июл" : [],
    "авг" : [],
    "сен" : [],
    "окт" : [],
    "ноя" : [],
    "дек" : [],
}

# 1. Наполнить словарь именами
# 1.1 Организация ввода
n = int(input().strip()) # Количество друзей, инфу о которых ...
for _ in range(n):
    name, _, month = input().strip().split() # ["Витя", "12", "дек"]
    # Добавить name в список в словаре month
    birthdays[month].append(name)
    
# 2. Организация вывода
m = int(input().strip()) # Количество запросов к записной книжке
for _ in range(m):
    month = input().strip() # Название месяца, по которому идет запрос
    # Используя month - вывести на консоль В ОТСОРТИРОВАННОМ ПОРЯДКЕ 
    # имена, хранимые по ключу month
    names =  birthdays[month]
    print(" ".join(sorted(names)))







