# 3
my_list=["abc","wert","bavd","aci","swa"]
new_list=[]
for element in my_list:
    if 'a' in element:
            new_list.append(element)
print(new_list)
#############################################

# 4
my_list=["abc",123,"wert","bavd",456,"aci",78,"swa"]
new_list=[]
for element in my_list:
    if type(element)==str:
        new_list.append(element)
print(new_list)
#############################################

# 5 сделал как вы реккомедуете, но с помощью count можно проверять
#   количество еллементов сразу в строке без создания множества
#   сделал оба варианта
my_str='adgsdghsgfgfasghjahaASJGDA'
my_set=set(my_str)
my_list=[]
for symbol in my_set:
    if my_str.count(symbol)==1:
        my_list.append(symbol)
print(my_list)
##############################################
# 5_1 (без множества)
my_str='adgsdghsgfgfasghjahaASJGDA'
my_list=[]
for symbol in my_str:
    if my_str.count(symbol)==1:
        my_list.append(symbol)
print(my_list)
##############################################

# 6
my_str_1='123456789ab56c'
my_str_2='jghklabnvg56c'
my_set_1=set(my_str_1)
my_set_2=set(my_str_2)
my_list=list(my_set_1.intersection(my_set_2))
print(my_list)
###############################################

# 7
my_list=[]
my_str_1='123456789ab56c'
my_str_2='jghklabnvg56c'
my_set_1=set(my_str_1)
my_set_2=set(my_str_2)
X_set=my_set_1.intersection(my_set_2)
for symbol in X_set:
    if my_str_1.count(symbol)==1 and my_str_2.count(symbol)==1:
        my_list.append(symbol)
print(my_list)