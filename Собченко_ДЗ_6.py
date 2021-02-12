# 1
# Задача решена с учетом того что первый элемент списка имеет порядковый
# номер НОЛЬ, а НОЛЬ это четное число так как делится на 2 без остатка
my_list=[str(symbol) for symbol in input('Введите элементы списка через пробел ').split()]
new_list=[]
index=0
while index<len(my_list):
    new_list.append(''.join(reversed(my_list[index]))) if index % 2 else new_list.append(my_list[index])
    index+=1
print(new_list)
###############################################

# 2
my_list=[str(symbol) for symbol in input('Введите элементы списка через пробел ').split()]
new_list=[]
for element in my_list:
     if element[0]=="a":
         new_list.append(element)
print(new_list)
###############################################

# 3
my_list=[str(symbol) for symbol in input('Введите элементы списка через пробел ').split()]
new_list=[]
for element in my_list:
    for symbol in element:
        if symbol=="a":
            new_list.append(element)
print(new_list)
################################################

# 4
my_list=[str(symbol) for symbol in input('Введите элементы списка через пробел ').split()]
new_list=[]
for element in my_list:
     if element.isdigit():
         new_list.append(element)
print(new_list)
################################################

# 5
my_list=[]
my_str=input("enter my_str ")
for symbol in my_str:
    if sum(1 for symbol_2 in my_str if symbol_2==symbol)==1:
       my_list.append(symbol)
print(my_list)
#################################################

# 6
my_list=[]
my_str_1=input('enter my_str_1 ')
my_str_2=input('enter my_str_2 ')
for symbol_1 in my_str_1:
    for symbol_2 in my_str_2:
        if symbol_1==symbol_2:
            my_list.append(symbol_1)
my_list=set(my_list)
print(my_list)
##################################################

# 7
my_list=[]
my_str_1=input('enter my_str_1 ')
my_str_2=input('enter my_str_2 ')
for symbol in my_str_1 :
    if my_str_1.find(symbol)-my_str_1.rfind(symbol)==0:
        if symbol in my_str_2 and my_str_2.find(symbol)-my_str_2.rfind(symbol) == 0 :
            my_list.append(symbol)
print(my_list)
##################################################

# 8
specific_person={"Фамилия":"Собченко",
                 "Имя":"Дмитрий",
                 "Возраст":31,
                 "Проживание":{"Страна":"Украина",
                               "Город":"Одесса",
                               "Улица":"Заболотного"},
                 "Работа":{"Наличие":"Да",
                           "Должность":"Каменщик"}}
###################################################

# 9
real_cake={"Кожи":{"Мука":"236 грамм",
                   "Молоко":"218 мл.",
                   "Масло": "75 грамм",
                   "Яйцо":"2 шт"},
           "Крем":{"Сахар":"30 грамм",
                   "Масло":"50 грамм",
                   "Ваниль":"0.5 ч.ложки",
                   "Сметана":"2 ст.ложки"},
           "Глазурь":{"Какао":"3 ст.ложки",
                      "Сахар":"5 ст.ложек",
                      "масло":"40 грамм"}}

