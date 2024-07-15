from os import system 
system ("clear")

# try:
#   num=int (input("Введение число: "))
#   print(num)
# except:
#    pass

# pass ничего не должен делать 

# try:
#   num=int (input("Введите число: "))
#   print(num)
# #   drtfghujiklp синтаксис  error
# except:
#    print("Ты написал не число.")

# #    except: предупредить 


# try:
#   num=int (input("Введите число: "))

# except ValueError:
#    print("Ты написал не число.")

# except NameError:
#    print("Не верное имя.")

# else:
#    print("Все написано верно.", num)

# finally:
#    print("Конец")


# 1 ошибка 
# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("Деление на ноль недопустимо.")
   
# 2
# try:
#     with open("несуществующий_файл.txt", "r") as file:
#        content = file.read()
# except FileNotFoundError:
#     print("Файл не найден.")
   

# 3
# user_input = "abc"
# try:
#        number = int(user_input)
# except ValueError:
#        print("Невозможно преобразовать в число.")
   
# #4 
# my_list = [1, 2, 3]
# try:
#        value = my_list[5]
# except IndexError:
#        print("Индекс вне диапазона.")
   


# # 5
# my_dict = {"name": "John", "age": 25}
# try:
#        value = my_dict["gender"]
# except KeyError:
#        print("Ключ не найден в словаре.")
   


# # 6
# from datetime import datetime
# date_str = "2023-01-01"
# try:
#        date_object = datetime.strptime(date_str, "%Y-%m-%d")
# except ValueError:
#        print("Некорректный формат даты.")
   


# # 7
# import sqlite3
# try:
#        connection = sqlite3.connect("несуществующая_бд.db")
# except sqlite3.Error as e:
#        print(f"Ошибка подключения к базе данных: {e}")
   


# 8
# numbers = [10, 5, 0, 8]
# results = []
# for num in numbers:
#        try:
#            result = 100 / num
#        except ZeroDivisionError:
#            result = "Деление на ноль"
#        results.append(result)
#        print(results)
   


# 9
# class CustomError(Exception):
#        pass

# try:
#        raise CustomError("Произошла ошибка")
# except CustomError as ce:
#        print(f"Поймано исключение: {ce}")
   



# 10
# try:
#         num1 = float(input("Введите первое число: "))
#         num2 = float(input("Введите второе число: "))
#         result = num1 / num2
#         print("Результат:", result)
# except ValueError:
#         print("Введите корректное число.")
# except ZeroDivisionError:
#         print("Деление на ноль недопустимо.")
    

# 1 задача
#  Попробуйте открыть файл "example.txt" для чтения и выведите его содержимое.
# Обработайте исключение, если файл не существует.
# try:
#     with open('example.txt', 'r') as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print("Файл не найден.")

# 2
# Попробуйте открыть файл "data.txt" для записи и запишите в него строку "Hello, World!".
# Обработайте исключение, если что-то пошло не так.
# try:
#     with open('data.txt', 'w') as f:
#         f.write('Hello, World!')
#         print("Запись выполнена успешно.")
# except  :
#     print("что-то пошло не так ")

# 3
# Напишите программу, которая запрашивает у пользователя имя файла и пытается открыть его для чтения.
# Если файл не существует, выведите соответствующее сообщение.
# try:
#    with open('имя файла.txt', 'r' )as f :
#       content = f.read()
#       print(content)
# except:
#    print("соответствующее сообщение.")

# 4
# Создайте функцию, которая принимает имя файла и возвращает количество строк в файле.
# Обработайте исключение, если файл не существует.

# try:
#  with open('filename.txt', 'r') as file:
#      lines = file.readlines()
#      print("len(lines")
# except FileNotFoundError:
#     print("Файл табылған жоқ.")


# 5
# Попробуйте открыть файл "config.txt" для чтения конфигурационных параметров.
# Если файл не найден, создайте новый с дефолтными параметрами.
# def read_or_create_config(filename):
#     default_config = {
#         'param1': 'value1',
#         'param2': 'value2',
#         'param3': 'value3'
#     }

#     try:
#         # Файлды ашу
#         with open(filename, 'r') as file:
#             config_data = file.read()
#             return config_data
#     except FileNotFoundError:
#         # Файл табылмаса, жаңа файл жасау және дефолттық параметрлермен жазу
#         with open(filename, 'w') as file:
#             for key, value in default_config.items():
#                 file.write(f"{key}={value}\n")
#         return "Жаңа файл жасалды және дефолттық параметрлер жазылды."

# # Функцияны сынау
# filename = 'config.txt'
# print(read_or_create_config(filename))







