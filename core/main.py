from os import system 
system("clear")
# n = 'hello world'

# text = 'sdkfjl;sd lkn kdsljfksd'
# count = 0
# for i in n:
#     count += 1
# print(count)

# count2 = 0
# for i in text:
#     count2 += 1
# print(count2)


# def len_word(word):
#     count = 0
#     for i in word:
#         count += 1
#     return count


# print(len_word('hello world'))
# print(len_word(text))


# def len_word(x):
#     count = 0
#     for i in x:
#         count += 1
#     return count

# b =  ''
# print(len_word(b))


# for i in range(1, 11):
#     if i == 3 or i == 5:
#         continue
#     if i == 8:
#         break
#     print(i)

# print('end')


# def main(x):
#     if x % 2 == 0:
#         return 'Это четное число'
#     return 'Это не четное число'

# n = int(input('Введите число: '))
# print(main(n))


# def is_even(x):
#     if x % 2 == 0:
#         return True
#     return False

# for i in range(1, 11):
#     if is_even(i):
#         print(i)

# n = 233
# count = 0
# for i in range(2, n):
#     if n % i == 0:
#         count = 1
#         break
# print(count)

# def is_prime(x):
#     count = 0
#     for i in range(2, x):
#         if x % i == 0:
#             count = 1
#             break
#     if count == 0:
#         return True
#     return False


# for i in range(1, 11):
#     if is_prime(i):
#         print(f'Простое число: {i}')
#     else:
#         print(f'Составное число: {i}')



# def main():
#     if 2 < 1:
#         print('Hello')
#     return 'Привет'
#     print('world')

# x = main()
# print(x)


### Задача 1: Сумма чисел в диапазоне
# Напишите функцию sum_range(start, end), которая 
# принимает два числа start и end и возвращает сумму всех 
# чисел в этом диапазоне, включая оба конца.

# def sum_range(start, end):
#     total = 0
#     for i in range(start, end + 1):
#         total += i
#     return total
# print(sum_range(1, 5))  # Шығару керек: 15
# print(sum_range(3, 7))  # Шығару керек: 25


# ### Задача 2: Поиск минимального числа в списке
# Напишите функцию find_min(numbers), которая принимает 
# список чисел и возвращает минимальное число в этом списке.

# def find_min(numbers):
#     if not numbers:
#         return None  # Егер тізім бос болса, None қайтарамыз.
    
#     min_number = numbers[0]  # Ең кіші сан ретінде алғашқы элементті аламыз.
#     for number in numbers:
#         if number < min_number:
#             min_number = number
#     return min_number
# print(find_min([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]))  # Шығару керек: 1
# print(find_min([-7, 0, 3, 4, 2, -8, 6]))  # Шығару керек: -8
# print(find_min([]))  # Шығару керек: None (бос тізім)


# ### Задача 3: Подсчет согласных
# Напишите функцию count_consonants(text), которая 
# принимает строку и возвращает количество согласных букв в 
# этой строке.

# def count_consonants(text):
#     consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
#     count = 0
    
#     for char in text:
#         if char in consonants:
#             count += 1
    
#     return count
# print(count_consonants("Hello, World!"))  # Шығару керек: 7
# print(count_consonants("Python is awesome!"))  # Шығару керек: 10
# print(count_consonants("AEIOU aeiou"))  # Шығару керек: 0


# ### Задача 4: Переворот строки
# Напишите функцию reverse_string(s), которая принимает 
# строку и возвращает её в перевернутом виде.

# def reverse_string(s):
#     return s[::-1]
# print(reverse_string("Hello, World!"))  # Шығару керек: !dlroW ,olleH
# print(reverse_string("Python"))  # Шығару керек: nohtyP
# print(reverse_string(""))  # Шығару керек: (бос жол)


# ### Задача 5: Проверка високосного года
# Напишите функцию is_leap_year(year), которая принимает 
# год и возвращает True, если год является високосным, и False 
# в противном случае.

# def is_leap_year(year):
#     if year % 400 == 0:
#         return True
#     if year % 100 == 0:
#         return False
#     if year % 4 == 0:
#         return True
#     return False
# print(is_leap_year(2000))  # Шығару керек: True (2000 жыл кібісе)
# print(is_leap_year(1900))  # Шығару керек: False (1900 жыл кібісе емес)
# print(is_leap_year(2024))  # Шығару керек: True (2024 жыл кібісе)
# print(is_leap_year(2023))  # Шығару керек: False (2023 жыл кібісе емес)


# ### Задача 6: Произведение всех элементов списка
# Напишите функцию product_of_list(numbers), которая 
# принимает список чисел и возвращает их произведение.

# def product_of_list(numbers):
#     if not numbers:
#         return 1  # Егер тізім бос болса, көбейтіндіні 1 деп аламыз.
    
#     product = 1
#     for number in numbers:
#         product *= number
#     return product
# print(product_of_list([1, 2, 3, 4, 5]))  # Шығару керек: 120
# print(product_of_list([10, -2, 3]))      # Шығару керек: -60
# print(product_of_list([7]))              # Шығару керек: 7
# print(product_of_list([]))               # Шығару керек: 1 (бос тізім)


# ### Задача 7: Проверка подстроки
# Напишите функцию contains_substring(s, substring), 
# которая принимает строку и подстроку, и возвращает True, 
# если подстрока содержится в строке, и False в противном 
# случае.

# def contains_substring(s, substring):
#     return substring in s
# print(contains_substring("Hello, World!", "World"))  # Шығару керек: True
# print(contains_substring("Python is awesome", "is"))  # Шығару керек: True
# print(contains_substring("OpenAI", "GPT"))  # Шығару керек: False
# print(contains_substring("Data science", ""))  # Шығару керек: True (бос ішкі жол барлық жолдардың ішінде бар деп есептеледі)


# ### Задача 8: Поиск индекса элемента
# Напишите функцию find_index(lst, element), которая 
# принимает список и элемент, и возвращает индекс элемента в 
# списке. Если элемент не найден, возвращает -1.

# def find_index(lst, element):
#     try:
#         return lst.index(element)
#     except ValueError:
#         return -1
# print(find_index([1, 2, 3, 4, 5], 3))  # Шығару керек: 2 (3 элементінің индексі)
# print(find_index(['a', 'b', 'c', 'd'], 'z'))  # Шығару керек: -1 (z элементі табылмады)
# print(find_index([10, 20, 30, 40, 50], 20))  # Шығару керек: 1 (20 элементінің индексі)

   
# ### Задача 9: Удаление пробелов
# Напишите функцию remove_spaces(s), которая принимает
# строку и возвращает эту строку без пробелов.

# def remove_spaces(s):
#     return s.replace(" ", "")
# def remove_spaces(s):
#     return ''.join([char for char in s if char != ' '])

# print(remove_spaces("Кездесуі керек, келесі мақсатқа өтініш беріңіз"))  # Шығару керек: "Кездесуікерек,келесімақсатқаөтінішберіңіз"
# print(remove_spaces("Ал бұл жағдай болмаса, менің сөзім көбі болады"))  # Шығару керек: "Албұлжағдайболмаса,меніңсөзімкөбіболады"
# print(remove_spaces("Программа жасаймыз"))  # Шығару керек: "Программажасаймыз"



# ### Задача 10: Проверка на число
# Напишите функцию is_number(s), которая принимает строку
# и проверяет, можно ли её преобразовать в число. Возвращает 
# True, если можно, и False в противном случае.

# def is_number(s):
#     try:
#         float(s)  # сөздікті санға ауыстыру
#         return True
#     except ValueError:
#         return False
# print(is_number("123"))    # Шығару керек: True
# print(is_number("3.14"))   # Шығару керек: True
# print(is_number("abc"))    # Шығару керек: False (сандық түрде емес)
# print(is_number("  45 "))  # Шығару керек: True (жарамды сандық мәнге айналды)





