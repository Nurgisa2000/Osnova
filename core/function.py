from os import system 
system("clear")

# def приветствие():
#     print('Привет, мир!')

# for i in range(101):
#     приветствие()

# приветствие()


# def validator_password(num):
#     print(num*3)

# validator_password(num=3)
# validator_password(num=5)
# validator_password(num=7)


# def validator_password(num,num2,num3,num4):
#     return num+num2+num3+num4  

# print(validator_password(
#     num=1,
#     num2=2,
#     num3=3,
#     num4=4
# ))
# # print(validator_password(num=5))
# # print(validator_password(num=7))

# # Создали функцию которая называется "name()" с параметром "first_name"
# def name(first_name): 
#     # Наша функция возврашает f"Привет{first_name}."
   
#     return f"Привет  {first_name.capitalize()}."

# # Мы запустили цикл где один и тот же код повторяется 2 раз 
# for i in range(2):
#     # Тут мы получаем имя пользователя с терминала с помощью  "input()"
#     # И сохраняем полученное имя в переменной "get_name"
#     get_name=input('Введение имя:')

#     print(name(get_name))




# def full_name (first_name,last_name, username="Unknown"):
#     return f"Hello {first_name} {last_name}. login:{username}"

# print(full_name('Marselle', 'Naz'))

# def database(iin=None):
#     if iin is None:
#         return "Вы забыли указать ИИН." 
    
#     user={
#         "000402500286":{
#             'namne':'Marselle',
#             'surname':'Naz'
#         }
#     }

#     if not iin.isdigit():
#         return "ИИН должен  состоять только из цифр."
    
#     elif len(iin)!=12:
#         return "ИИН должен содержать 12 цифр."
    
#     else:
#         return user.get(iin, "ИИН не найден.") 

# get_iin=input("Введите ИИН: ")
# print(database(get_iin))



# validator_password
# Получить пароль от пользователя
# Повторить получения пароля
# Проверить длину пароля
# Проверить, что в пароле есть цифры
# Проверить, что в пароле есть буквы в нижнем регистре
# Проверить, что в пароле есть буквы в верхнем регистре
# Проверить, что в пароле есть спец. символы !@#$%^&*()_+>?<

def validator_password(password, password2):
    if password !=password2:
        return "Пароли не совпадают."
    
    if len (password)<8: 
        return f"Пароль слишком короткий. {len(password)}"
    
    validator_password= "Nurgis2@"
    return "Пароль жарамды."

    # Проверка наличия букв в нижнем регистре
    char_lowers=False
    for char in password:
        if char.islower():
            char_lowers=True
            break

   
    # Проверка наличия букв в верхнем регистре
    char_uppers = False
    for char_u in password:
        if char_u.isupper():
            char_uppers = True
            break
    
    char_punctuation = False
    for char_p in password:
        if char_p in "!@#$%^&*()_+>?<":
            char_punctuation = True
            break

    if char_lowers == False:
        return "В пароле нет нижнего регистра."
    
get_p=input("Пароли : ")
get_p2=input("Пароли : ")
print(validator_password(get_p, get_p2))