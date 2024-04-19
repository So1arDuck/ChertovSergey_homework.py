immutable_var = (1, 2, 3, "undying", True)
print(immutable_var)
immutable_var [0][1] = 4
print(immutable_var) ## Кортежи внутри списка являются неизменяемыми элементами(!)
# Но он может содержать внутри изменяемые объекты. Изменению подвержена только часть
# внутри скобок, основная часть кортежа неприкосаема.
mutable_list = ([1, 2, 3.14, "fearless", False])
print(mutable_list)
mutable_list[2] = "Duck"
print(mutable_list)
mutable_list[3] = 0.45
print(mutable_list)















# metal = ["silver", "gold", "coins", 'brave', 'curiosity']
# print(metal[1])
# metal[1] = "susal"
# print(metal)
# metal.append(True) - Добавляет эллемент в конец списка
# print(metal)
# metal.extend('cosmos') #\ metal.extend('cosmos', 12)
# print(metal)
# metal.remove('coins')
# print(metal)
# print('silver' in metal)
# print(metal[0:4])

# tuple_1 = 1, 2, 3, 4
# print(tuple_1)
# tuple_2 = (1, 2, 3, 4)
# print(tuple_2)
# tuple_3 = ([1, 2], 5)
# print(tuple_3)

# tuple_ = ([1, 2], 0) + (1, 2) - Изменению подвержена только часть внутри скобок, основная часть кортежа неприкосаема.
# print(tuple_)
# tuple_[0][1] = 4
# print(tuple_)
# tuple_ = (1, 2) * 5
# print(tuple_)