import os 
os.system('clear')


# def my_decorator(func):
#     def wrapper():
#         print('Start function')
#         print(func())
#         print('End function')
#     return wrapper

# @my_decorator
# def hello():
#     return 'hello world!'

# @my_decorator
# def hhh():
#     return 'hhh'

# hello()
# hhh() 


# В Python декоратор-это специальная конструкция,
# которая позволяет изменять поведение  функции или метода, 
# к которому он применяется
# from time import time 

# def timing_decorator(func):
#     def  wrapper():
#         start_time = time() # Фиксируем запуск
#         func()
#         end_time = time() # Фиксируем остановку
#         print(f'Func {func.__name__} worked {end_time - start_time}')

#     return wrapper

# @timing_decorator
# def hello():
#     return 'hello world'
# hello()


# рекурсия 
# Рекурсия Python - это техникаб при  которой функция вызывает
# саму себя в процессе выполнения. 

# def func(n):
#     print(n)
#     if n<=1:
#        return 0
    
#     return func(n-1)

# print(func(10))




