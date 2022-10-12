# Пример : счетчик символов в строке
# Пользователь вводит произвольную строку
# Задача: вывести на консоль сколько раз каждая буква входит
# в эту строку


message = "Hollo world!"
counter = {}

# Iteration Letter       Dict
# -         -            {}
# 0         H            Проверяю, входит ли H в ключи? Нет? Тогда добавляю пару {H : 1}
# 1         o            -//- {H:1, o:1}
# 2         l            -//- {H:1, o:1, l:1}
# 3         l            {H:1, o:1, l:2}
# 4         o            {H:1, o:2, l:2}
for letter in message:
    if letter in counter.keys():
        counter[letter] = counter[letter] + 1 # counter["l"] = counter["l"] + 1 =2
    else:
        counter[letter] = 1 # counter["l"] = 1

for k, v in counter.items():
    print(k, v)

print(counter)