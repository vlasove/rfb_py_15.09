# "Виртуальные" области видимости

# Пример на c++ (завершается ошибкой, т.к. b определена внутри тела условного оператора - а это тело - и есть отдельная область видимости)

# int a = 10;

# if (a > 8) {
#     int b = 10;
# }

# print(b);

# Тот же пример на Python

a = 10
b = 0

if a > 8:
    b = 20 # Переменная определенная внутри тела условного оператора - попадает в общий стек пременных программы!

print(b)


# Аналогично с циклами
value = 0
while True:
    value = 10
    break

print(value)