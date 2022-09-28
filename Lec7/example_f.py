# Решение задачи L

message = input()
print(message)

i = 0
while True:
    if len(message) < 3:
        break
    if i % 2 == 0:
        message = message[2:]
    else:
        message = message[:-2]

    print(message)
    i += 1