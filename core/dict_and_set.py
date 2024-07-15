# my_list=[
# 1,2,3
# ]

# my_tuple=(
#     1,2,3
# )

# print(my_list)
# print(my_list[0])
# print(my_list[0:1])


# text="       hello        "

# print(text)
# print(text.strip())

# my_set={
#     1,3,2,7,8,1,2, "hello" 
# }


# my_list1=[1,2,2,2,3,3,5,7,5,4,3]

# print(
#     list(set(my_list1_))
# )
      

# a={1,2,3,4}
# b={3,4,5,6,7}

# print(
#     a.isdisjoint(b)#пересекается false не пересекается true
#  )

# print(
#     a.union(b),#обьединение 

#     a|b
# )

# print(a.intersection(b))# возвращает пересечение
# print(a&b)

# print(b.difference(a)) #разность
# print(a.difference(b)) #разность
# print(b-a) #разность

# print(a.symmetric_difference) #симметрическая разность

# my_set2={1}

# my_set2.add(1)
# my_set2.add('hello')
# my_set2.add('jake')
# my_set2.add('bob')

# my_set2.remove('bob')
# my_set2.pop() # удалить первый элемент
# my_set2.clear()# очистит но так как нельзя оставить пустым вернет интерператора 

# print(my_set2)

#Api-Dictinary - Dict- dict()

my_dict={
    'bmw':{
        'volume': 4.4,
        'model': 'bmv m5 f90'
    },
    'mers':{
        'volume': 4.4,
        'model': 'E63 213',
        'mileage': 90000,
    }
}

my_dict.update({"subaru": "marselle"})
                
print(my_dict['subaru'])

# print(my_dict.items())
# print(my_dict['mers'].keys())
# # print(my_dict['mers'].values())
# print(my_dict.get('weather','нет такого ключа.'))

# my_dict['mers']['mileage']+=1000

# print(
#     my_dict['mers']
# )

# usres={
#     'marselle':'steam',
#     'madiar':'whatsapp,
# }
# users.update({'altynbek':"telegram"})

# usres['dariga']='insta'

# print(usres)

a = {
    1:2,
    2: 'hello str', #str
    3:[1,2,3,], ## list
    4:[1,2,3,],#tuple
    5:True,#blue
    5:None,
    6:None,
    7:7.7, #b=float
    8: {
       'city':'Almaty'
}
}

print(a[3][1])
print(a[4][2])
print(a[8]['city'])

