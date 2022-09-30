# Начало решения задачи B

COMMAND_TO_PUSH_BACK = "Кто последний?"
COMMAND_TO_PUSH_TO_HEAD = "Я только спросить!"

queue = []
n_commands = int(input().strip())

for _ in range(n_commands):
    command = input().strip()
    if COMMAND_TO_PUSH_BACK in command:
        # Кто последний? Я - Кузнецов. -> Кузнецов
        words = command.split(" - ") # ["Кто последний? Я", "Кузнецов."]
        lastname = words[-1].replace(".", "") # "Кузнецов." (ТОЧКА ЛИШНЯЯ) -> Необходимо избавиться от точки!
        lastname = words[-1][:-1]
        lastname = words[-1].split(".")[0] # ["Кузнецов", ""][0]
        queue.append(lastname)
    elif COMMAND_TO_PUSH_TO_HEAD in command:
        #Я только спросить! Я - Иванова. -> Иванова
        words = command.split(" - ") # ["Я только спросить! Я", "Иванова."]
        lastname = words[-1].replace(".", "") # "Иванова." (ТОЧКА ЛИШНЯЯ) -> Необходимо избавиться от точки!
        lastname = words[-1][:-1]
        lastname = words[-1].split(".")[0] # ["Иванова", ""][0]
        queue.insert(0, lastname)
    else: # Следующий!
        if len(queue) != 0 :
            print(f"Заходит {queue.pop(0)}!") # Выдаем самого первого в очереди
        else:
            print("В очереди никого нет.")

