# from os import system
# system("clear")

# import os

# for i in range(10):
#     # os.mkdir(f"folder_{i}")
#     os.system(f'rm -rf folder_{i}')



# os.system("mkdir a s d f")

# os.system("rm -rf a s d f")

# os.system("ls")

# os.system("mkdir Hello")

# os.system("rm -rf Hello")

# os.mkdir("Hello")
# os.remove("Hello")



# date-хранить дату
# time - хранить время
# datetime- хранит дату и время 

import datetime

from datetime import datetime as dt

# date=dt.now().date()
# time=dt.now().time()
# date_time=dt.now()

# print(date)
# print(time)
# print(date_time)

# %H - Час
# %M - Минута
# %S - Секунда
# %d - День
# %m - Месяц
# %Y - Год (2024)
# %y - Год (24)

# date_time=dt.now().strftime("%H:%M:%S  %d.%m.%y")
# print(date_time)

# day=dt.now().day
# month=dt.now().month
# year=dt.now().year

# hour=dt.now().hour
# minute=dt.now().minute
# second=dt.now().second

# print(
#     day,
#     month,
#     year,
# )


# import random, os

# my_list=[
#     'Мадияр', 'Дарига', 'Шахусейн', 
#     'Темирлан', 'Алтынбек', 'Илья',
#     'Нурай', 'Нургиса', 'Марсель',
#     'Магамед'
# ]

# while len(my_list)!=1:
#     os.system('clear')
#     user = random.choice(my_list)
#     # if user == 'Марсель':
#     #     continue
#     # else:
#     my_list.remove(user) 

#     print(f"Выбыл пользователь: {user}")
#     input("Enter to continue... ")
# else:
#     print('Победитель:', my_list[0])

# my_list.remove(random.choice(my_list))
# print(my_list)


# my_list.remove("Марсель")
# print(my_list)


# print(
#     random.choice(my_list)
# )



# import random 

# a=[1,2,3,4,5,6,7,8,9]

# random.shuffle(a)
# print(
#     a  
# )
# 8,10
# # print(
#     random.randrange(0,10,2)
# )



# print(
#     random.randint(90,100) #диапозон от и до 
# )


# print(
#     random.choices (a,k=3)
# )


# print(
#     random.sample (a, 2) # не повторяет 
# )




