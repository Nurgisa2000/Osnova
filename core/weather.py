# import requests, os

# # GET - получить - READ

# # POST - отправить - CREATE
# # PUT - изменить - UPDATE
# # DELETE - удалить - DELETE
# # responce = requests.post()
# # responce = requests.put()
# # responce = requests.delete()

# appid = '1327e58b44062a45b570ed26a0356900'
# city=input('Введите город: ')
# URL = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={appid}&units=metric&lang=ru"

# responce=requests.get(url=URL).json()

# data = responce

# country=data['sys']['country']
# description=data['weather'][0]['description']
# temp=data['main']['temp']
# feels_like = data['main']['feels_like']
# humidity=data['main']['humidity']
# speed=data['wind']['speed']
# visibility=data['visibility']

# os.system('clear') 

# text=f"""
# Страна: {country}
# Город: {city}
# Описание:{ description.capitalize()}.
# Температура: {temp} C.
# Ощущается как: {feels_like} C.
# Влажность: {humidity} %.
# Скорость ветра: {speed} м/с.
# Видимость: {visibility} м.

# """
# print(text)




from os import system 
system("clear")

# Калькуляторды іске асыру
def calculator():
    while True:
        # Кіру сұрақтарын көрсету
        print("Қандай операцияны орындау керектігін таңдаңыз:")
        print("1. Қосу (+)")
        print("2. Алу (-)")
        print("3. Көбейту (*)")
        print("4. Бөлу (/)")
        print("5. Шығару")
        
        # Пайдаланушыдан операцияны таңдау
        choice = input("Операцияның нөмірін енгізіңіз (1/2/3/4/5): ")
        
        # Пайдаланушы шығару операциясын таңдаса, циклді түсіріп шығамыз
        if choice == '5':
            print("Калькуляторды жабу")
            break
        # Кіру сандарын сұрау
        num1 = float(input("Бірінші санды енгізіңіз: "))
        num2 = float(input("Екінші санды енгізіңіз: "))
        # Көрсетілген операцияны орындау
        if choice == '1':
            result = num1 + num2
        elif choice == '2':
            result = num1 - num2
        elif choice == '3':
            result = num1 * num2
        elif choice == '4':
            # Егер екінші санды 0-ге бөлсеңіз, қате болады
            if num2 == 0:
                print("Қате! Нольге бөлу мүмкін емес.")
                continue
            result = num1 / num2
        else:
            print("Жарамсыз операция нөмірін енгіздіңіз.")
            continue
        # Нәтижені шығару
        print("Нәтиже: ", result)
# Калькуляторды іске асыру
calculator()