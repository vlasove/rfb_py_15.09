# Синтаксис одиночного условного оператора
# if expression:
#     body

# age = int(input())

# if age >= 18:
#     print("Welcome!")   # 4 spacing 
#     print("Second line")

# print("Program exit")


age = int(input())

if age >= 18:
    print("Your age is:", age)
    print("Welcome to our service!")
    print("Press here to continue!")
    if True:
        print("Inner body")
        if True:
            print("Inner body 2")

print("Service done!")