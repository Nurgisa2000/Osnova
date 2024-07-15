# full_name="Nurgisa Abd"
# print(full_name.lower(),  ':lower')# все буквы меняет на маленкий 
# print(full_name.upper(),  ':upper')# все буквы меняет на большое 
# print(full_name.title(),  ':title')#меняет первую букву на заглавную слово

# #меняет первую букву предложения на верхний регистр
# print(full_name.capitalize(),':capitalize')

# #посчитать сколько по строк в строке
# print(full_name.count('e'),':count')

#  swapcasere большой буквы поменяет на маленькое. маленькое буквы поменяет на большое 
# print(full_name.swapcasere(),':swapcasere)

# text="привет,111 как у тебя  дела? "

# #метод для замены:что заменить и на что заменить 
# print(text.replace('1',''), ':replace')

# first_name=input("Нвпиши имя.")
# adress=input("напиши адрес:")
# phone_number = input("Напиши номер телефона:")


# first_name="Nurgisa"
# adress="AlfaraBI"
# phone_number = "+77779704859"

# user_info=f"""
# Имя:{first_name}
# Адрес:{adress}
# Телефон:{phone_number}
# """
# print(user_info)

# name="Нургиса"

# # text=f"меня зовут {name}."
# text="Меня зовут {a} {b}.".format(a=name,  b=1)
# print(text)


test_text="sdfddsd"
#проверяет, все ли написано в нижнем регистре
print(test_text.islower(),":islower")

#проверяет все ли написано в верхнем регистре 
print(test_text.isupper(),":isupper")

# биринши арип улкен болу 
print(test_text.istitle(), ":istitle")

#пробел пустой если одно буквы фолсе
print(test_text.isspace(), ":isspace")

#проверяет написано лс строка слитно
print(test_text.isidentifier(), ":isidenfier")

#проверяет яыляется ли строка цифрой
print(test_text.isdigit(), ":isdigit")


#проверяет яыляется ли строка только буквами
print(test_text.isalpha(), ":isalpha")

#проверяет яыляется ли строка цифрой или буквами
print(test_text.isalnum(), ":isalnum")

#проверяет яыляется ли строка числами 
# isnumeric==isdigit
print (test_text.isnumeric(), ":isnumeric")

#прверяет является ли строка float 
print (test_text.isdecimal(), ":sdecimal")


 
