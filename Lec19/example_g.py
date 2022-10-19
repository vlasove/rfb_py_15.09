"""
Запись нескольких строк в файл
"""

messages = ["\nHello", "World", "!"]
fh = open(file="output.txt", mode="a")
fh.writelines([message + "\n\n" for message in messages]) # ["Hello\n\n", "World\n\n", "!\n\n"]
fh.close()

with  open(file="output.txt", mode="a") as fh:
    fh.write("\nNew line in with manager")