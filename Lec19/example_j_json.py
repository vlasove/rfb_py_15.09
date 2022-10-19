import json

json_data = None
with open("data.json", mode="r") as fh:
    json_data = json.load(fh) # .load() - "вычитывание" / десериализация

print('From json:', json_data)
print(type(json_data))

DATA = {
    "name" : "Alex",
    "last_name" : "Smirnov",
    "link" : "https://vk.com/accounts/?user=14213413.php"
}

GENERAL_DATA = {
    "first" : DATA,
    "second": [10, 20, 30, False, None, {"a":"a"}],
}


with open("data3.json", "w") as fh:
    json.dump(obj=GENERAL_DATA, fp=fh, indent=4) # "запись" / сериализация
