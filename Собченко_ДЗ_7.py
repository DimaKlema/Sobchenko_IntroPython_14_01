import random as rnd

# 1
my_list=[rnd.randint(1,100) for i in range(20)]
#####################################################

# 2
triangle={'A':[rnd.randint(-10,10) for i in range(3)],
          'B':[rnd.randint(-10,10) for i in range(3)],
          'C':[rnd.randint(-10,10) for i in range(3)]}
######################################################

# 3
def my_print(string):
    print((string.center(len(string)+6,'*')))
my_print(input())
######################################################

# 4 За основу взяты имена и возраст некоторых астронавтов побывавших на луне =)
younger_list=[]
name_list=[]
persons=[{'name':'Nill','age':39},{'name':'Buzz','age':39},{'name':'Mike','age':38},
         {'name':'Charles','age':34},{'name':'Harrison','age':34}]
for person in persons:
   younger_list.append(person.get('age'))
   name_list.append(person.get('name'))
index=0
while index<len(younger_list):
    if younger_list[index]==min(younger_list):
        print(' Младший ',persons[index].get('name'))
    index+=1
index_name=0
while index_name<len(name_list):
    if len(name_list[index_name])==len(max(name_list,key=len)):
        print('самое длинное имя ',name_list[index_name])
    index_name+=1
print('средний возраст космонавтов ', sum(younger_list)/len(younger_list),'лет')
####################################################

# 5
my_list_a=[]
my_list_b=[]
my_list_1=[]
my_list_2=[]
new_dict={}
x_dict={}
my_dict_1={'страна':"Украина","город":"Одесса","улица":"Заболотного","дом":44}
my_dict_2={'страна':"Украина","город":"Киев","почта":"7777@почта.юа","телефон":"0977777777"}
for key_1 in my_dict_1.keys():
    my_list_1.append(key_1)
    for key_2 in my_dict_2.keys():
        my_list_2.append(key_2)
        if key_1==key_2:
            my_list_a.append(key_1)# список из ключей, которые есть в обоих словарях
my_list_b=[word for word in my_list_1 if word not in my_list_2]#с писок из ключей, которые есть в первом, но нет во втором словаре
print('a) ',my_list_a)
print('б) ',my_list_b)
for word in my_list_b:
    new_dict[word]=my_dict_1.get(word)# новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре
print("в) ",new_dict)
x_dict={**my_dict_1,**my_dict_2}# объединяю словари
for key in my_list_a:# изменяю полученый словарь под правило из условия
    x_dict[key]=[my_dict_1.get(key),my_dict_2.get(key)]
print("г) ",x_dict)


