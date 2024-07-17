from os import system
system("clear")  # Очищает экран терминала (работает только в терминале, не в IDE).

# Не изменяемые
# str - ''           # Строка
# int - 1            # Целое число
# float - 1.1        # Число с плавающей точкой
# bool - True, False # Логическое значение
# tuple - ()         # Кортеж

# None
# frozenset - frozenset() # Неизменяемое множество

# Изменяемые
# list - []         # Список
# set - {}          # Множество
# dict - {}         # Словарь

# text = "     Im HUM,AN       "

# # Метод title() делает первую букву каждого слова заглавной.
# print(text.title())  # '     Im Hum,An       '

# # Метод upper() делает все буквы заглавными.
# print(text.upper())  # '     IM HUM,AN       '

# # Метод lower() делает все буквы в нижнем регистре.
# print(text.lower())  # '     im hum,an       '

# # Метод capitalize() делает первую букву заглавной из всего текста.
# print(text.capitalize())  # '     im hum,an       '

# # Метод swapcase() меняет регистр букв.
# print(text.swapcase())  # '     iM hum,an       '

# # Метод replace() заменяет указанную подстроку на другую подстроку.
# print(text.replace("HUMAN", "Programmer"))  # '     Im HUM,AN       ' (нет точного совпадения с "HUMAN")

# # Метод strip() удаляет пробелы с начала и конца строки.
# print(text.strip())  # 'Im HUM,AN'

# # Метод lstrip() удаляет пробелы с начала строки.
# print(text.lstrip())  # 'Im HUM,AN       '

# # Метод rstrip() удаляет пробелы с конца строки.
# print(text.rstrip())  # '     Im HUM,AN'

# # Метод split() разделяет строку на части по пробелам.
# print(text.split())  # ['Im', 'HUM,AN']

# # Метод find() находит первое вхождение подстроки и возвращает его индекс, или -1 если не найдено.
# print(text.find('I'))  # 5

# # Метод rfind() находит последнее вхождение подстроки и возвращает его индекс, или -1 если не найдено.
# print(text.rfind('I'))  # 5

# # Метод index() находит первое вхождение подстроки и возвращает его индекс, или вызывает ValueError если не найдено.
# print(text.index('I'))  # 5

# # Метод rindex() находит последнее вхождение подстроки и возвращает его индекс, или вызывает ValueError если не найдено.
# print(text.rindex('I'))  # 5

# # Метод startswith() проверяет начинается ли строка с указанной подстроки и возвращает True или False.
# print(text.startswith('I'))  # False

# # Метод endswith() проверяет заканчивается ли строка указанной подстрокой и возвращает True или False.
# print(text.endswith(' '))  # True

# name = "marselle"

# # Метод isalpha() проверяет состоит ли строка только из букв и возвращает True или False.
# print(name.isalpha())  # True

# # Метод isdigit() проверяет состоит ли строка только из цифр и возвращает True или False.
# print(name.isdigit())  # False

# # Метод isnumeric() проверяет состоит ли строка только из числовых символов и возвращает True или False.
# print(name.isnumeric())  # False

# # Метод isalnum() проверяет состоит ли строка только из букв и цифр и возвращает True или False.
# print(name.isalnum())  # True

# # Метод isspace() проверяет состоит ли строка только из пробелов и возвращает True или False.
# print(name.isspace())  # False

# # Метод istitle() проверяет написано ли каждое слово в строке с заглавной буквы и возвращает True или False.
# print(name.istitle())  # False

# # Метод isupper() проверяет состоит ли строка только из заглавных букв и возвращает True или False.
# print(name.isupper())  # False

# # Метод islower() проверяет состоит ли строка только из строчных букв и возвращает True или False.
# print(name.islower())  # True

# # Метод isidentifier() проверяет является ли строка допустимым идентификатором в Python и возвращает True или False.
# print(name.isidentifier())  # True

# # Метод isascii() проверяет состоит ли строка только из ASCII символов и возвращает True или False.
# print(name.isascii())  # True

# # Метод isprintable() проверяет состоит ли строка только из печатных символов и возвращает True или False.
# print(name.isprintable())  # True

# # Метод isdecimal() проверяет состоит ли строка только из десятичных цифр и возвращает True или False.
# print(name.isdecimal())  # False




# a = ['marselle',              'naz',                        'aza']
# # Метод join() объединяет элементы списка в строку, разделяя их указанным разделителем.
# print(" ".join(a))  # 'marselle naz aza'





# isinstance (my_list, list )

# my_list=["marselle", 1, 1.2, True, False, {1,2,3,}, {'name': 'marselle'}, (1,2)]

# my_list=[1,2,3,4,5]
# my_list=my_list
# # my_list=list('lkjhgv') 
  
# isinstance(my_list, list)

# my_list = [1, 2, 3, 4, 5]
# my_list_2 = [7, 8]
# # my_list1 = list('maslkdm')

# # Добавление элемента в конец списка
# my_list.append(6)
# print(my_list)  # [1, 2, 3, 4, 5, 6]

# # Расширение списка
# my_list.extend(my_list_2)
# print(my_list)  # [1, 2, 3, 4, 5, 6, 7, 8]

# # Вставка элемента на позицию
# my_list.insert(6, "Что добавить")
# print(my_list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8]

# # Удаление элемента
# my_list.remove('Что добавить')
# print(my_list)  # [0, 1, 2, 4, 5, 6, 7, 8]

# # Удаление и возврат элемента по индексу
# last_element = my_list.pop(7)
# print(last_element)  # 8
# print(my_list)       # [0, 1, 2, 4, 5, 6, 7]

# # Очистка списка
# my_list.clear()
# print(my_list)  # []

# my_list = [1, 3, 2, 4, 5]

# # Поиск индекса элемента
# index_of_three = my_list.index(3)
# print(index_of_three)  # 2

# # Подсчет вхождений элемента
# count_of_twos = my_list.count(2)
# print(count_of_twos)  # 1

# # Сортировка списка
# my_list.sort()
# print(my_list)  # [1, 2, 3, 4, 5]

# # Сортировка в обратном порядке
# my_list.sort(reverse=True)
# print(my_list)  # [5, 4, 3, 2, 1]

# test_list = [1, 'sksk', 3, 4, "sk", 10]

# # Разворот списка
# test_list.reverse()
# print(test_list)  # [1, 2, 3, 4, 5]

# # Копирование списка
# my_list_copy = test_list.copy()
# print(my_list_copy)  # [1, 2, 3, 4, 5]


# # a = [1, 2, 3, 4, 5]

# # b = a.copy()  # Создание копии списка
# # b.append(6)

# # print(a)
# # print(b)


# tuple
# my_tuple = (1, 1, True, 2, 3, 4, 5)
# # Создаем кортеж my_tuple, который содержит значения: 1, 1, True, 2, 3, 4, 5.

# my_tuple_2 = tuple('hello')
# # Создаем кортеж my_tuple_2, который содержит символы строки 'hello': ('h', 'e', 'l', 'l', 'o').

# my_tuple_3 = 1, 2
# Создаем кортеж my_tuple_3, который содержит значения: 1 и 2.

# print(my_tuple.index(1))
# Находим индекс первого вхождения значения 1 в кортеже my_tuple и выводим его. (Закомментировано)

# print(my_tuple.count(1))
# Считаем количество вхождений значения 1 в кортеже my_tuple и выводим его. (Закомментировано)

# print(my_tuple_2.index('e'))
# Находим индекс первого вхождения символа 'e' в кортеже my_tuple_2 и выводим его. (Закомментировано)

# print(my_tuple_2[my_tuple_2.index('e')])
# Находим индекс первого вхождения символа 'e' в кортеже my_tuple_2 и выводим значение по этому индексу. (Закомментировано)

# print(my_tuple_2[1])
# Выводим значение по индексу 1 из кортежа my_tuple_2. В данном случае это будет 'e'. (Закомментировано)

# print(my_tuple_3)
# Выводим кортеж my_tuple_3. В данном случае это будет (1, 2). (Закомментировано)

# a, b = my_tuple_3
# Распаковываем кортеж my_tuple_3 в две переменные: a и b. a будет равно 1, b будет равно 2. (Закомментировано)

# print(a)
# Выводим значение переменной a, которое равно 1. (Закомментировано)

# print(b)
# Выводим значение переменной b, которое равно 2. (Закомментировано)





# set, dict
# print(my_set)
# print(my_set_2)

# # В set нельзя хранить list, dict и set то есть изменяемые типа данных
# my_set = {2, 1, 3, 4, 5}
# my_set_2 = set('marselle')

# # Основные методы множества

# # Добавляет элемент в множество.
# my_set.add(6)

# # Удаляет элемент из множества. 
# # Если элемент не найден, вызывает исключение KeyError.
# my_set.remove(1)

# # Удаляет элемент из множества, если он существует. 
# # Если элемент не найден, ничего не делает.
# my_set.discard(41)

# # Удаляет и возвращает случайный элемент из множества.
# random_element = my_set.pop()
# # print(random_element)
# # print(my_set)

# # Очищает множество.
# my_set.clear()
# # print(my_set)  # set()

# # Создает копию множества.
# my_set_copy = my_set.copy()
# # print(my_set_copy)  # set()

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}

# # Возвращает объединение множеств.
# union_set = set1.union(set2)
# print(union_set)  # {1, 2, 3, 4, 5}
# # Объединение
# print(set1 | set2)  # {1, 2, 3, 4, 5}

# # Возвращает пересечение множеств.
# intersection_set = set1.intersection(set2)
# print(intersection_set)  # {3}
# # Пересечение
# print(set1 & set2)  # {3}

# # Возвращает разность множеств
# difference_set = set1.difference(set2)
# difference_set2 = set2.difference(set1)
# print(difference_set)  # {1, 2}
# print(difference_set2)  # {1, 2}
# # Разность
# print(set1 - set2)  # {1, 2}

# # Возвращает симметрическую разность множеств.
# sym_diff_set = set1.symmetric_difference(set2)
# print(sym_diff_set)  # {1, 2, 4, 5}
# # Симметрическая разность
# print(set1 ^ set2)  # {1, 2, 4, 5}

# # Проверяет, является ли текущее множество подмножеством другого.
# print(set1.issubset({1, 2, 3}))  # True

# # Проверяет, является ли текущее множество надмножеством другого.
# print(set1.issuperset({1, 2}))  # True

# # Проверяет, не пересекаются ли множества.
# print(set1.isdisjoint(set2))  # False



# # Проверка принадлежности элемента:
# print(1 in set1)  # True
# print(4 in set1)  # False





# словарь (dictionary) — это неупорядоченная коллекция пар ключ-значение. 
# Каждый ключ в словаре уникален и ассоциирован с некоторым значением. 
# Словари используются для хранения данных в формате, 
# удобном для быстрого доступа и манипуляции.

# Создание словаря
# Словари создаются с использованием фигурных скобок {} или функции dict().

# # Пустой словарь
# empty_dict = dict() or {}

# # Словарь с элементами
# my_dict = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }

# Основные методы словаря

# dict[key]: Доступ к значению по ключу.
# name = my_dict["name"]
# print(name)  # Alice

# # dict[key] = value: Установка значения по ключу.
# my_dict["age"] = 31
# print(my_dict)  # {'name': 'Alice', 'age': 31, 'city': 'New York'}


# get(key[, default]): Возвращает значение по ключу, если ключ существует, 
# иначе возвращает default.

# my_dict = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }

# age = my_dict.get("age")
# age = my_dict.get("age", 12)
# age = my_dict.get("age", 'Нет токо-го ключа.')
# print(age)  # 30

# country = my_dict.get("country", "Kazakhstan")
# print(country)  # Kazakhstan

# # keys(): Возвращает все ключи словаря.
# keys = my_dict.keys()
# print(keys)  # dict_keys(['name', 'age', 'city'])

# # values(): Возвращает все значения словаря.
# values = my_dict.values()
# print(values)  # dict_values(['Alice', 31, 'New York'])

# # items(): Возвращает все пары ключ-значение.
# items = my_dict.items()
# print(items)  # dict_items([('name', 'Alice'), ('age', 31), ('city', 'New York')])

# # pop(key[, default]): Удаляет и возвращает значение по ключу.
# city = my_dict.pop("city")
# print(city)  # New York
# print(my_dict)  # {'name': 'Alice', 'age': 31}

# # popitem(): Удаляет и возвращает последнюю добавленную пару ключ-значение.
# last_item = my_dict.popitem()
# print(last_item)  # ('age', 31)
# print(my_dict)  # {'name': 'Alice'}

# # clear(): Очищает словарь.
# my_dict.clear()
# print(my_dict)  # {}

# # update([other]): Обновляет словарь, добавляя пары ключ-значение из other.
# my_dict = {"name": "Alice", "age": 30}
# my_dict.update({"age": 31, "city": "New York"})
# print(my_dict)  # {'name': 'Alice', 'age': 31, 'city': 'New York'}


  
# person = {
#     "name": "Bob",
#     "age": 25,
#     "job": "Developer"
# }

# # Создание и доступ к элементам:
# print(person["name"])  # Bob
# print(person.get("name"))  # Bob
# print(person.get("name1", "Bob"))  # Bob

# # Добавление и изменение элементов:
# person["age"] = 50
# person["age1"] = 50
# print(person)  # {'name': 'Bob', 'age': 50, 'job': 'Developer'}

# # Проверка наличия ключа:
# # if "city" in person.keys():
# if "city" in person:
#     print("Key exists")
# else:
#     print("Key doesn't exist")

# # Итерирование по словарю:
# for k, v in person.items():
#     # print(f"{k}: {v}")
#     print(k)
#     print(v)

# # Удаление элементов:
# del person["job"]
# print(person)  # {'name': 'Bob', 'age': 50, 'age1': 50}

# city = person.pop("city", "Unknown")
# print(city)  # Unknown
# print(person)  # {'name': 'Bob', 'age': 50, 'age1': 50}

# # Очищение словаря:
# person.clear()
# print(person)  # {}

# # Создание словаря
# my_dict = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }

# # Доступ к значению по ключу
# print(my_dict["name"])  # Alice

# # Установка значения по ключу
# my_dict["age"] = 31
# print(my_dict)  # {'name': 'Alice', 'age': 31, 'city': 'New York'}

# # Получение значения по ключу с использованием get
# print(my_dict.get("city"))  # New York
# print(my_dict.get("country", "USA"))  # USA

# # Все ключи, значения и элементы
# print(my_dict.keys())    # dict_keys(['name', 'age', 'city'])
# print(my_dict.values())  # dict_values(['Alice', 31, 'New York'])
# print(my_dict.items())   # dict_items([('name', 'Alice'), ('age', 31), ('city', 'New York')])

# # Удаление элемента
# print(my_dict.pop("city"))  # New York
# print(my_dict)  # {'name': 'Alice', 'age': 31}

# # Удаление последнего элемента
# print(my_dict.popitem())  # ('age', 31)
# print(my_dict)  # {'name': 'Alice'}

# # Очистка словаря
# my_dict.clear()
# print(my_dict)  # {}

# # Обновление словаря
# my_dict.update({"name": "Alice", "age": 30})
# print(my_dict)  # {'name': 'Alice', 'age': 30}


# database = {
#     'marselle': {
#         'bank': {
#             'balance': 1000,
#             'card_number': '4440 4200 1313 3333',
#             'recvisit': '78765456789098765',
#         },
#         'account': {
#             'instagram': {
#                 'login': 'marselle.naz',
#                 'password': 'JKNJKasddas22',
#             },
#             'telegram': {
#                 'login': 'MarselleNaz',
#                 'phone': '+7 747 056 06 06',
#             }
#         },
#         'info': {
#             'first_name': 'Marselle',
#             'last_name': 'Naz',
#             'age': 21,
#         },
#         'address':'Moskva Lenina 1',
#     }
# }


#  Получение информации о пользователе:
# marselle_info=database['marselle']['info']

# print(
#      marselle_info['first_name'],
#      marselle_info['last_name'],
#      marselle_info['age']
# )

# balance=database['marselle']['bank']['balance']
# balance+=1000
# print(balance)

# instagram_login=database['marselle']['account']['instagram']['login']
# instagram_password=database['marselle']['account']['instagram']['password']

# print(instagram_login) # marselle.naz
# print(instagram_password) # password


# Изменеие пароля Instagram: 
# Обновление адрес:
# Добавление новой учетной записи в account- 'github':{'login':'marselle', 'password':'123ws'} 
# Dобавление новой информации в info- 'email':'mars@gmail.com':
# удаление адрес:

# # database сөздігінің Instagram паролін өзгерту
# instagram=database['marselle']['account']['instagram']

# instagram.update(
#     {'login':'mars.naz','password':'123', }
# )

# print(instagram)

# # database сөздігінің account-ға жаңа жазба қосу
# account=database['marselle']['account']['github'] = {'login': 'marselle', 'password': '123ws'}
# account.update(
#     {'github': {'login': 'marse11e', 'password': 'XXXXX'}}
# )

# print(account)



# database сөздігінің info-да жаңа мәлімет қосу
# database['marselle']['info']['email'] = 'mars@gmail.com'

# # database сөздігінен адрес мәнін жою
# if 'address' in database['marselle']['info']:
    # del database['marselle']['info']['address']

# Нәтижені тексеру
# print("Current database:", database)







# Уровень 8.1 задачника Python №1
# from urllib.parse import urlparse

# url = 'http://test.com/dir1/dir2/dir3/page.html'

# # URL-ді талдау
# parsed_url = urlparse(url)

# # Домен атын алу
# domain_name = parsed_url.netloc

# print(domain_name)


# 2
# Берілген тізім
# my_list = [
#     [1, 2, 3],
#     [1, 2],
#     [1, 2, 3, 4, 5],
#     [1],
#     [1, 2, 3, 4],
# ]

# # Сұрыптау
# sorted_lists = sorted(my_list, key=len)

# print(sorted_lists)


# 3
# Берілген тізім
# my_list = [
#     [2, 4, 5],
#     [1, 2, 3],
#     [0, 1, 1],
#     [5, 7, 1],
# ]

# # Сұрыптау
# sorted_list = sorted(my_list, key=sum)

# print(sorted_list)


# 4
# Пирамиданы шығару
# for i in range(1, 6):
    # print('x' * i)


# Уровень 8.2 задачника Python №1
# from urllib.parse import urlparse

# url = 'http://test.com/dir1/dir2/dir3/page.html'

# # URL-ді талдау
# parsed_url = urlparse(url)

# # Жолдың соңғы бөлігін алу
# page_name = parsed_url.path.split('/')[-1]

# print(page_name) 


# 2
# Берілген тізім
# my_list = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
# ]

# # Сандарды біріктіру
# result = [int(''.join(map(str, sublist))) for sublist in my_list]

# print(result)  


# 3
# Пирамиданы шығару
# for i in range(1, 6):
#     print('x' * (i * 2))

# Уровень 8.3 задачника Python №1
# from urllib.parse import urlparse

# url = 'http://test.com/dir1/dir2/dir3/page.html'

# # URL-ді талдау
# parsed_url = urlparse(url)

# # Протоколды алу
# protocol = parsed_url.scheme

# print(protocol)  


# 2
# lst = [1, 2, 3, 4, 5, 6]
# num = 3

# square_num = num ** 2  # num аймақтың квадратын есептеу

# # Тізімдің ұзындығы квадрат мәнімен тең болатынша бос жолдарды қосу
# for _ in range(square_num - len(lst)):
#     lst.append('')

# print(lst)

# # 3
# for i in range(1, 10):
#     print(str(i) * 3)



# Уровень 8.4 задачника Python
#1
# import urllib.parse

# url = 'http://test.com/dir1/dir2/dir3/page.html'

# URL мекен-жайынан папкаларды алу
# parsed_url = urllib.parse.urlparse(url)
# folders = parsed_url.path.split('/')[1:-1] 
 # '/' бойынша бөлініп алған соң босталғыш / және 
 # page.html аластатын алғашқы өріснен кейінгі өріске дейініп аяқталады



#  2
# for i in range(1, 10):
    # print(str(i) * i)


# 3
# data = [
#     {
#         'country': 'country1',
#         'city':    'city11',
#     },
#     {
#         'country': 'country2',
#         'city':    'city21',
#     },
#     {
#         'country': 'country3',
#         'city':    'city31',
#     },
#     {
#         'country': 'country1',
#         'city':    'city12',
#     },
#     {
#         'country': 'country1',
#         'city':    'city13',
#     },
#     {
#         'country': 'country2',
#         'city':    'city22',
#     },
#     {
#         'country': 'country3',
#         'city':    'city32',
#     },
# ]

# # Бос сөздермен толтырылатын жаңа ағымдағы өзгеріс
# result = {}

# for item in data:
#     country = item['country']
#     city = item['city']
    
#     if country in result:
#         result[country].add(city)
#     else:
#         result[country] = {city}

# # Ағымдағы өзгеріс жасалған структура
# print(result)







# цикл for while

# my_list={
#     'используется для итерации по последовательности',
#     'В каждом проходе цикла переменная',
#     'Python поддерживает два типа циклов',
# }

# a=[]

# for i in my_list:  # Tuple, Set, List
#     a.extend(i.split()) 

# print(a)

# for i in my_list:
    #  if i.startswith('Python'):
        #  print(i)


# Итерация по строке 
# for letter in "banana": #по буквам
    #  print(letter)


# a=[]

# for sentence in my_list:
#     print(sentence)
#     for letter in sentence:
#         print(letter) 


# word=''

# # Итерация по строке 
# for letter in "banana": #по буквам
#     if letter =='a':
#       word += letter.upper()
#     else:
#        word += letter
    
# print(word) # bAnAnA


# # Использование функции range()
# for i in range(10):
#   word += str(i)

# print(word)



# a = {
#     'balance': 1000,
#     'card': {'name': 'ask', 'a':1},
#     'recvisit': '7875',
# }


# for k, v in a.items():
#     print(k)
#     print(v)


# for k, v in a['card'].items():
#     print(k)
#     print(v)



# Цикл while в Python используется для выполнения блока кода 
# многократно до тех пор, пока условие остается истинным то есть True.

# while условие:
#     блок_кода

# count = 0

# while count < 10:
#     print(count)
#     count += 1

# while True:
#     print("Этот цикл будет выполняться вечно")


# count = 0
# while count < 10:
#     if count == 5:
#         break
#     print(count)
#     count += 1


# count = 0

# while count < 10:
#     print(count)
#     count += 1
# else:
#     print("Цикл завершен")

# count = 0
# while count < 10:
#     count += 1
#     if count % 2 == 0:
#         continue
#     print(count)



# # В Python есть множество встроенных функций, 
# # которые предоставляют базовые операции и функциональность,
# # не требующую дополнительного импорта модулей.

# # Функция print() используется для вывода данных на экран.
# print("Hello, World!")

# # Функция len() возвращает количество элементов в объекте 
# # (например, в списке, строке, кортеже и т.д.).
# my_list = [1, 2, 3, 4, 5]
# print(len(my_list))  # Вывод: 5

# # Функция type() возвращает тип объекта.
# a = 5
# print(type(a))  # Вывод: <class 'int'>

# # Эти функции используются для преобразования типов данных.
# num_str = "123"
# num_int = int(num_str)
# num_float = float(num_str)
# num_str_back = str(num_int)

# print(num_int)       # Вывод: 123
# print(num_float)     # Вывод: 123.0
# print(num_str_back)  # Вывод: "123"

# # Функция sum() возвращает сумму элементов в итерируемом объекте.
# numbers = [1, 2, 3, 4, 5] # Tuple, List, Set
# print(sum(numbers))  # Вывод: 15

# # Функции max() и min() возвращают максимальное и минимальное 
# # значение из итерируемого объекта соответственно.
# numbers = [1, 2, 3, 4, 5] # Tuple, List, Set
# print(max(numbers))  # Вывод: 5
# print(min(numbers))  # Вывод: 1

# # Функция sorted() возвращает новый отсортированный 
# # список из итерируемого объекта.
# letter = ['f', 'd', 'a', 'c', 'b']
# numbers = [5, 2, 3, 1, 4]
# print(sorted(letter))  # Вывод: ['a', 'b', 'c', 'd', 'f']
# print(sorted(numbers))  # Вывод: [1, 2, 3, 4, 5]
# print(sorted(letter, reverse=True)) 
# print(sorted(numbers, reverse=True)) 

# # Функция range() возвращает последовательность чисел, 
# # которая часто используется в циклах.
# for i in range(5):
#     print(i)
# # Вывод: 0 1 2 3 4

# # Функция enumerate() добавляет счетчик к итерируемому объекту и 
# # возвращает его в виде объекта перечисления.
# fruits = ["apple", "banana", "cherry"]
# for i, f in enumerate(fruits): # Tuple, List, Set
#     print(i, f)
# # Вывод:
# # 0 apple
# # 1 banana
# # 2 cherry

# # Функция zip() используется для объединения двух или более итерируемых 
# # объектов в один итератор кортежей.
# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]

# for n, a in zip(names, ages):
#     print(f"{n} is {a} years old")
# # Вывод:
# # Alice is 25 years old
# # Bob is 30 years old
# # Charlie is 35 years old

# # Функция filter() применяет функцию к каждому элементу итерируемого 
# # объекта и возвращает итератор с элементами, для которых функция вернула True.
# numbers = [1, 2, 3, 4, 5, 6]
# even_numbers = filter(lambda x: x % 2 == 0, numbers)
# print(list(even_numbers))  # Вывод: [2, 4, 6]  # Tuple, List, Set


# # def ekmf(x):
# #     if x % 2 == 0:
# #         return True
# #     else:
# #         return False

# # numbers = [1, 2, 3, 4, 5, 6]

# # print(list(filter(ekmf, numbers)))

# # Функция map() применяет функцию к каждому элементу итерируемого объекта 
# # и возвращает итератор с результатами.
# def squared(x):
#     return x ** 2

# numbers = 'a l k s n d k l a s d'.split()
# squared_numbers = map(str.upper, numbers)
# # Tuple, List, Set
# print(list(squared_numbers))  # Вывод: [1, 4, 9, 16, 25]

# # Функции all() и any() возвращают True, если все или хотя бы 
# # один из элементов итерируемого объекта истинны соответственно.
# bool_list = [True, True, False]
# print(all(bool_list))  # Вывод: False
# print(any(bool_list))  # Вывод: True

# # Функция input() считывает строку из стандартного ввода (например, из консоли).
# # name = input("Enter your name: ")
# # print(f"Hello, {name}!")

# # Функция open() используется для открытия файла
# # и возвращает соответствующий объект файла.
# # with open("example.txt", "w") as file:
# #     file.write("Hello, World!")


# Лямбда-функции в Python (также называемые анонимными функциями) 
# это небольшие одноразовые функции, которые определяются с использованием 
# ключевого слова lambda. Они могут принимать любое количество аргументов, 
# но имеют только одно выражение. 

# lambda аргументы: выражение

# # Обычная функция
# def add(x, y=1):
#     return x + y

# # Лямбда-функция
# add_lambda = lambda x, y=1: x + y

# # Использование
# print(add(2, 3))          # Вывод: 5
# print(add_lambda(2, 3))   # Вывод: 5




# Условия в одну строку в Python называются тернарными операторами 
# или условными выражениями. 
# Они позволяют записывать условные конструкции if-else в компактной форме.


# Синтаксис тернарного оператора
# значение_если_истинно if условие else значение_если_ложно

# a = 1

# bool_type = True if a == True else False
# print(bool_type)

# x = 10
# y = 20

# max_value = x if x > y else y
# print(max_value)  # Вывод: 20

# a = 5
# b = 3

# print("a больше b" if a > b else "a не больше b")  # Вывод: a больше b

# # Тернарные операторы можно вкладывать друг в друга, но это может ухудшить читаемость кода.
# x = 5
# y = 10
# z = 15

# result = "x наибольший" if x > y and x > z else "y наибольший" if y > z else "z наибольший"
# print(result)  # Вывод: z наибольший

# # Использование тернарного оператора в функциях
# def get_status(age):
#     return "взрослый" if age >= 18 else "несовершеннолетний"

# print(get_status(20))  # Вывод: взрослый
# print(get_status(15))  # Вывод: несовершеннолетний



# Цикл в листе, или list comprehension, в Python – это удобный и читаемый 
# способ создания новых списков, применяя выражение к каждому элементу 
# итерируемого объекта. List comprehensions могут включать условные выражения 
# для фильтрации элементов. то есть тернарные условия

# Синтаксис
# [выражение for элемент in итерируемый_объект if условие else continue]

# выражение: выражение, которое будет применено к каждому элементу.
# элемент: текущий элемент итерируемого объекта.
# итерируемый_объект: объект, по которому будет проходить цикл (например, список, строка, диапазон и т.д.).
# условие (необязательно): фильтр для включения только тех элементов, которые удовлетворяют условию.

# numbers_even = [x for x in range(1, 10) if x % 2 == 0]
# print(numbers_even)  # Вывод: [2, 4, 6, 8]

# names = ['marselle', 'ilya', 'madiyar']
# e_in_name = [i for i in names if 'i' in i]
# print(e_in_name)

# text = "hello"
# char_list = [char for char in text]
# print(char_list)  # Вывод: ['h', 'e', 'l', 'l', 'o']

# print([num for num in range(1, 10)])
# print(list(range(1, 10)))
# print(list("hello"))

# **kwargs dict

def имя(параметры):
    # тело функции
    pass

имя('аргументы')


def func(name):
    return f"Hello, {name}"

# print(func("Marselle"))

def func1(num, num2=10):
    return num + num2

# print(func1(5, 5))


def func2(num, num2=10, *args):
    return num + num2 + sum(args)

# print(func2(5, 5, 3, 3, 3, 1))


def func2(num, num2=10, *args, **kwagrs):
    print(kwagrs)
    return num + num2 + sum(args) + kwagrs['age']

# print(func2(5, 5, 3, 3, 3, 1, age=20))


def func3(num, num2=10, *args, **kwagrs):
    print(kwagrs)
    return num + num2 + sum(args) + len(kwagrs['name'])

print(func3(5, 5, 3, 3, 3, 1, name='marselle'))














