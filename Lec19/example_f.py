"""
Запись строки в файл
"""

message = "10000000"
fh = open(file="output2.txt", mode="a") # mode="w" - перезапись, "а" - дозапись
fh.write(message)
fh.close()