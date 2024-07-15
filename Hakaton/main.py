import os
os.system('clear')

#1 
# print("Hello word")
# 2
# name=str(input('Write your name: '))

# age=str(input('write your age: '))
 
# print(f"Привет,Write your name: {name}! Тебе write your age: {age} лет.")

# 3
# number = int(input("Введи число: "))
# if (number % 2 == 0):
#    print("Четное ")
# else:
#    print("Не четное")
# 
#4
# a = int(input("Введи число: "))

# if a > 0:
#     print('Положительное')
# elif a == 0:
#     print("Ноль")
# else:
#     print('Отрицательное')

# 5
  
# строка = input("Введите строку: ")

# обратная_строка = строка [::-1]

# print("Обратная строка: ", обратная_строка )

# 6.

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# четные = []

# for i in numbers:
#     if i % 2 == 0:
#         четные.append(i)

# print(четные)


# 7  
# num1 = float(input("Введите первое число: "))
# num2 = float(input("Введите второе число: "))

# сумма = num1+num2

# print("Сумма: ", сумма)

# 8

# lst = []
# for i in range(1,11 ):
#     lst.append(i ** 2)

# print(lst)


# # 9
# lst = []
# for i in range(1, 10):
#     if i < 5:
#         continue
#     else:
#         lst.append(i)
# print(lst)

#10 

# string = [
#     "adsf",
#     "yyfadwjks"
#     "eagqhw",
#     "daerwuusbnnx"
# ]

# for i in string:
#     if len(i) > 8:
#         print(i)


# # 11

# a = 0

# while a >= 0:
#     a = int(input("Write number: "))
#     if a >= 0:
#         print(a)

# print("Negative")

# 12

# tup = ('sdfghj', 'wertgbvn', 'sdfgh', 'zsedcfgb', 'sdrfvc')

# for i in tup:
#     print(i.upper())


# 13
# slovar = {
#     'altynbek': 87076698869,
#     'marselle': 87077770101,
#     'ilya': 87011500550,
#     'nurgisa': 87770077007
# }

# print(slovar[input('Write your name: ').lower()])
# 

# 14

# s1 = input("Please enter a string1: ")
# s2 = input("Please enter a string2: ")
# print(set(s1 + s2))

# 15
# def factorial(num):
#     summ = 1
#     for i in range(1, num + 1):
#         summ *= i
#     return summ

# print(factorial(7))

# 16.
# def sentence(name, **kwargs):
#     print(f"Привет {name}")
#     for i, x in kwargs.items():
#         print(f"{i}: {x}")
# sentence("Imya", age = "20", city = "Gorod")


# 17. 
# def magazin():
#     data = {}  
    
#     while True:
#         touch = input("Введите '1', чтобы добавить, '2', чтобы узнать общую сумму, или '3', чтобы выйти: ")
 
#         if touch == '1':
#             item = input("Введите название: ")
#             price = int(input("Введите цену: "))
#             data[item] = price
#             print(f"Товар {item} добавлен в корзину")  
#         elif touch == '2':
#             total = sum(data.values())
#             print(f"Общая сумма покупок: {total}")      
#         elif touch == '3':
#             print("Выход")
#             break      
#         else:
#             print("Попробуйте снова")
# magazin()
        

# 20.

# table = input("""

#     Реализация функции для управления городами пользователей.

#     Пользователь может:
#     1. Добавить нового пользователя.
#     2. Обновить город существующего пользователя.
#     3. Удалить пользователя из списка.
#     4. Вывести список всех пользователей с их городами.
#     >>> """)


# data = {
#     'altynbek': 'Almaty',
#     'ilya': 'Astana',
#     'zhansultan': 'Aktobe',
#     'nurgisa': 'Aktau'
# }

# def manage_cities(city_dict: dict):
#         if table == '1':
#             new_name = input('Введите имя: ')
#             new_city = input('Введите город: ')
#             city_dict[new_name] = new_city
#             return f'Ваше имя сохранено {city_dict}'
#         elif table == '2':
#             name = input('Введите имя: ')
#             new_city = input('Введите город: ')
#             city_dict[name] = new_city
#             return f'Ваш город обновлен {city_dict}'
#         elif table == '3':
#             name = input('Введите имя: ')
#             del city_dict[name]
#             return f'Вы удалены {city_dict}'
#         elif table == '4':
#             return city_dict
#         else:
#             return 'Введите правильное число'
# print(manage_cities(data))


# 