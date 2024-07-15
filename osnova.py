import os 
os.system('clear')

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
my_tuple = (1, 1, True, 2, 3, 4, 5)
# Создаем кортеж my_tuple, который содержит значения: 1, 1, True, 2, 3, 4, 5.

my_tuple_2 = tuple('hello')
# Создаем кортеж my_tuple_2, который содержит символы строки 'hello': ('h', 'e', 'l', 'l', 'o').

my_tuple_3 = 1, 2
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

