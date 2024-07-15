from os import system
system('clear')

# def fucn(num, num2=10):
#     return num+num2


# print(fucn(10))
# 1 обязатеьные параметры (n,a)
# 2 по умолчанию(n,2,name='marsele', age=21)
# 3 случайные (n,a, name='marsele', age=21, *args, **kwarg)

# Случайный параметр * args хранит данные в типе Tuple, данный не изменный порядке 
# def all_students(a, b=10, *args): # 1)обязатеьные параметры, 2)по умолчанию, 3)*args
#      return args # тип данных тюпл, много аргумент , любой тип данных, хранит всегда тюпл 

# print(all_students('marselle', 'dasha', 'dima', 'ilya', 
#  ))


# a=[1,2,3,4]

# b=[*a,5,6]

# c=[11,10]

# c.append(a)
# print(c)
# print(b)

# *args позволяет передавать произвольное количество позиционных 
# аргументов в функцию. Эти аргументы передаются как Tuple.

# **kwargs позволяет передавать произвольное количество именованных (ключевых) 
# аргументов. Эти аргументы передаются как Dict.
 

# def user_info(a,b=10,*args,**kwargs):
#     return [a,b,args, kwargs]
# print(user_info(
#      'marsele',21,1,2,3, 123123, name='marsele', age=21
# ))


# def user_info(**kwargs):
#     return kwargs

# r=(user_info(
#     name='marsele', age=21
# ))

# r={'name': 'marsele', 'age':21}

# def func2(name, age):
#     return f'Name is {name}, age is {age}'

# print(func2(**r))
# # print(func2(r['name], r['age]))


# def sum_int(*args):
#     # (1,2,3,4)
#    count=0
#    for i in args:
#     #    if type(i)==int:
#     #        count+=i
#     #     else:
#     #        continue
#         if isinstance(i,int):
#            count +=i
#         else:
#            continue
#    return count 

# print(sum_int(1,2,3,4,5))

# int
# I
# L-a
# a=1


# def complex_calculations(a,b,*args): #def complex_calculations функция 
#     if isinstance(a,int,) and isinstance(b,int):
#         result = a+b # (2+3)=5 # натиже шыгарады
        
#         for num in args: #бұл цикл арқылы args тізіміндегі әрбір элемент тексеріледі.
#             if not isinstance(num,int):
#                 continue
#             else:
#                 #5*num
#                 #num=4
#                 result *=num
#         return result
#     else:
#         return "a and b is not int" # бутин сан емес деп аударылады 

# print(complex_calculations(2,3,4)) #курдели есептеулер 
# # Бұл функция екі аргументтің (a және b) бүтін сан (integer) екенін тексереді. 
# # Егер олар бүтін сан болса, олардың қосындысын есептейді (2 + 3 = 5). 
# # Содан кейін қосымша аргументтердің (args) әрқайсысы бүтін сан болса, 
# # оларды нәтиже (result) мәнімен көбейтеді. Соңында нәтиже қайтарылады. 
# # Егер a немесе b бүтін сан болмаса, "a және b бүтін сан емес" деген хабарламаны қайтарады.



# def n(a,b):
#     return a+b

# n = lambda a, b=10: a + b
# n1 = lambda a, b=10: a / b
# n2 = lambda a, b=10: a * b
# n3 = lambda a, b=10: a - b

# print(n(2))
# print(n1(2))
# print(n2(2))
# print(n3(2))



# a=[1,2,3,4]
# iter- Итерируемый тип данные 
# int, float, bool не итерируются  
# print (
#     len(a) #len- Встроенная фукнция которая считает длину iter типа данных 
# )
# print(
#     sum(a) #sum - Встроенная функция которая возращает  
#     # сумму массива (list, tuple, set)
# )
# print(
#     sorted(a) #sorted- Встроенная функция которая сортирует массив 
# )
# a = [1, 2, 3, 4]: a айнымалысына тізім (list) беріледі.
# iter - Итерируемый тип данных: iter - Итерирленген мәлімет типі.
# int, float, bool не итерируются: int, float, bool итерирленген тип емес.
# len(a): len - Ішкі функция, итерирленген типтің ұзындығын есептейді.
# sum(a): sum - Ішкі функция, массивтің (list, tuple, set) қосындысын қайтарады.
# sorted(a): sorted - Ішкі функция, массивті сұрыптайды.


# my_list = [0,1,2, False, True, "gg"]

# print(
#     any(my_list) # если хоть один True то вернет True 
# )
# print(
#     all(my_list) # если все True, вернет True
# )



# def print_person_info(**kwargs):
#     for k, v in kwargs.items():  
#         print(k, v)
# # print_person_info(name='marselle', age=21, city='Moscow')

# def avg_age(**kwargs):
#     return sum(kwargs.values()) / len(kwargs)
# # avg_age=lambda **kwargs:sum(kwargs.values())/len(kwargs)
# print(avg_age(
#     ilya       =48,
#     madiyar    =29,
#     nurgisa    =24,
#     magamed    =24,
#     marselle   =21,
#     shahhusein =21,
#     dariga     =19,
#     altynbek   =17,
#     zhansultan =16,
#     nurai      =16, 
#     temirlan   =14,  
# ))

# # Дано
# names=[
#     'ilya ','madiyar', 'nurgisa',
#     'magamed', ' marselle', 'shahhusein',
#     'dariga ','altynbek ', 'zhansulta ', 
#     'nurai', 'temirlan  '
# ]
# # Барлық есімдерді бір жолға біріктіру
# combined_names = ''.join(names).replace(" ", "")

# # 'a' әрпінің санын анықтау
# a_count = combined_names.count('a')

# print(f"Біріктірілген есімдер: {combined_names}")
# print(f"'a' әрпінің саны: {a_count}")

# # Метод join() 
# # необходимо сложить все имена и посчитать сколька букв 'a'
# # встречается в именах 


# Уровень 1.1 задачника Python
# 1 задача Дано число. Проверьте, отрицательное оно или нет. 
# Выведите об этом информацию в консоль. 
# def print_check_number(number):
#     if number < 0:
#         print(f"{number} теріс сан")
#     else:
#         print(f"{number} теріс емес сан")

# print_check_number(7)
# print_check_number(-7)

#2  задача  Дана строка. Выведите
# в консоль длину этой строки. 
# def print_string_length(s):
#     length = len(s)
#     print(f"Жолдың ұзындығы: {length}")

# print_string_length("Nurgisa123")


# 3 задача  Дана строка. Выведите в 
# консоль последний символ строки. 
# def print_last_character(s):
#     last_char = s[-1]
#     print(f"Соңғы символ: {last_char}")

# print_last_character("Nurgisa")

# 4 задача Дано число. 
# Проверьте, четное оно или нет. 
# def check_even_or_odd(number):
#     if number % 2 == 0:
#         print(f"{number} жұп сан")
#     else:
#         print(f"{number} тақ сан")

# check_even_or_odd(2)
# check_even_or_odd(-1)

# 5задача. Даны два слова. Проверьте, 
# что первые буквы этих слов совпадают. 
# def print_check_first_letters(word1, word2):
#     if word1[0].lower() == word2[0].lower():
#         print("Бірінші буквы сәйкес")
#     else:
#         print("Бірінші буквы сәйкес емес")

# print_check_first_letters("Nurgisa", "nurgisa")

# 6 задача  Дано слово. Получите его последнюю букву. 
# Если слово заканчивается на мягкий знак,
# то получите предпоследнюю букву. 

