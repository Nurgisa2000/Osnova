#тема урока for and while

# for i in ['name',2,True]: #каждый элемент вернется
#     print(i)

# for i in range (1,10):
#     print(i)

# names=['Мадияр', 'Дарига', 'Шахусейн', 'Темирлан', 'Алтынбек', 'Илья', 'Нурай', 'Нургиса', 'Марсель']\

# for i in names:
#     if i == 'Марсель':
#         break # остановить 
#     else:
#         print("привет", i)


# names=['Мадияр', 'Дарига', 'Шахусейн', 'Темирлан', 'Алтынбек', 'Илья', 'Нурай', 'Нургиса', 'Марсель']\

# for i in names:
#     if i == 'Марсель':
#         continue # пропустить 
#     else:
#         print("привет", i)

# text= "Привет, сегодня было жарко.".split()

# print(text)

# for i in text:
#     print(i)
# цикл 
# text= "Привет, сегодня было жарко.".split() #split пробел каждый боледи 

# print(text)

# for i in text:
#     if i =='было':
#        print(i)

#        for j in i: # было j просто быро думали 
#           print(j)

#     else:
#        continue

# my_list=[]

# for i in range (1,11):
#     my_list.append("apple")

# print(my_list)

# my_list=[]

# for i in range (1,11):
#     name=input(f"введение фрукт {i}:")
#     my_list.append(name)

# print(my_list)

# my_list=[]
# name=input("Введение фруктов через пробел:")
# my_list=name.split()
# print(my_list)

#list set tuple str - dic object is iterable 
# float int bool object is not iterable
# for i in 4.4:
#     print(i) 
# # 
# data={
#     'name':'Madira',
#     'age':16,
#     'job':'Student'
# }

# for k, v in data.items():  ##.items():-ключи и значение 
#     # print(k)
#     print(k,v)
#     print(v)

# names=['Мадияр', 'Дарига', 'Шахусейн', 'Темирлан', 'Алтынбек', 'Илья', 'Нурай', 'Нургиса', 'Марсель']

# for i in names:
#     print(i)

# num = [1,2,3,4,5 ] #15
# #1+2+3+4+5=15

# sum=0

# for i in num:
#     sum=sum+i

# print(sum)

# for i in range(0,12):
#     if i % 2 ==0:
#       print(i)  

# words = ['Мадияр', 'Дарига', 'Шахусейн', 'Темирлан', 'Алтынбек']

# for word in words:
#     print(word, ":", len(world))

# my_list=[]

# for num  in range(1,101):
#     if num % 2 !=0:
#         my_list.append(num)
# print(my_list)

# words=[]

# for i in range(1,200):
#     print(words)
#     word=input("Введение слово:")

#     if len(word)>5:
#        words.append("длинное")

#     else:
#        words.append("короткое")
# print(words)

# d=[]

# for i in range (1,10):
#     for j in range (1,10):
#         print(f"{i}*{j}={i*j}")

# my_list=[]

# for i in range(1,11):
#     if i%2==0:
#         my_list.append(i**2)

# print(my_list)


# a=0
# for i in range (1,11):
#     a+=1

# print(a) 


# while True:
#     pass

# sum = 0
# for i in text:
#     if i in [",", " ", "?"]:
#         continue

#     sum += 1

# print(sum)



# text = "Привет"

# for i in text[::-1]:
#     print(i)

# for i in range(1, 11):
#     print(text*i)


# for i in range(1, 10):
#     for j in range(1, 10):
#         print(f"{i} * {j} = {i*j}")

# Задача: Создайте список, который содержит квадраты всех чисел от 1 до 10, 
# но только для четных чисел. 
# Описание: Эта задача требует создания списка, 
# который содержит квадраты всех четных чисел от 1 до 10. 
# Это можно сделать с помощью цикла for и оператора 
# if для проверки четности числа.

# my_list = []

# for i in range(1, 11):
#     if i % 2 == 0:
#         my_list.append(i**2)


# print(my_list)

# a = 0
# for i in range(1, 11):
#     a += 1


# users = {}
# erorrs_password = ["123", 'qwerty', 'asd', 'llll', '1234567890']

# username = input("Введите имя: ")
# password = input("Введите пароль: ")
# password_2 = input("Повторите пароль: ")

# while password != password_2 or password in erorrs_password:
#     A1 = "Пароли не совпадают!"
#     A2 = "У вас слишком простой пароль!"
#     A3 = A1 + " - " + A2

#     if password != password_2:
#         print(A1)
#     elif password in erorrs_password:
#         print(A2)
#     else:
#         print(A3)

#     password = input("Введите пароль: ")
#     password_2 = input("Повторите пароль: ")

# else:
#     print("Пароль успешно принят!")

#     users["username"] = username
#     users["password"] = password
#     print(users)

 # a = 1
 # while True:
 #     print(a)
 #     a *= 2

