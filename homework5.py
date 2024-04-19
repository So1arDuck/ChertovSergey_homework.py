tools = ["hammer", "mallet", "pliers", "hacksaw", "screwdriver"]
print(tools)
tools[0]
print(tools[0])
print(tools[-1])
print(tools[2:6])
tools[2] = "warm"
print(tools)

my_dict = ({"hammer": "молоток", "mallet": "киянка", "pliers": "плоскогубцы","hacksaw": "ножовка"})
print(my_dict)
print(my_dict.values())
my_dict.update ({"screwdriver": "шуруповерт"})
print(my_dict)


# list = [1, 2, 3]
# list.pop(0)
# print(list)

#***Есть способ разделять такие задания? Создавать подзаголовок?***

# phone_book = {'Gloria':89996661455, 'Vladimir':89996661477}
# print(phone_book["Gloria"]) # Тип ковычек не влияет на вывод данных.
# phone_book['Gloria'] = 1234567890
# print(phone_book)
# phone_book['Valeria'] = 1325476980 # Так как это список, то он подвержен измненениям, и его можно корректировать в любой момент времени.
# print(phone_book)
# del phone_book['Vladimir'] # В список можно как добавлять, так и удалять в любой момент написания.
# print(phone_book)
# phone_book.update({'Franco': 1452789632,
#                    'Dorian': 1256987435})
# print(phone_book.keys()) #- Достает для нас "ключи" - имена
# print(phone_book.values()) #- Достает для нас "значения"
# print(phone_book.items()) #- Создает пару ключ-значение