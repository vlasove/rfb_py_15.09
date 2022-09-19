# Решение задачи H

# while True:
#     word = input()
#     if word == "": # терминальное условие
#         break
#     print(word)


# Часть решения задачи I

while True:
    first_password = input()
    second_password = input()

    if len(first_password) < 8:
        print("Слишком короткий пароль!")
    elif "123" in first_password or "qwe" in first_password:
        print("Слишком простой пароль!")
    elif first_password != second_password:
        print("Введенные пароли различаются!")
    else:
        print("Ну наконец-то!")
        break   