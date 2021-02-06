# 1
zero=0 # zero-искомое количество нулей
number=input(" введи целое число  ")
for symbol in str(number):
    if symbol=="0":
        zero=zero+1
print(zero)
##########################################

# 2
number=int(input("Введи число "))
if number==0:
    print(1)
    exit()
zero = 0
while number%10==0:
    number//=10
    zero +=1
print('В конце введенного числа',zero,"нуля")
###########################################

# 3a
index_1=1
index_2=0
my_list_1=[1,2,3,4,8]
my_list_2=[6,7,8,9,11]
my_result=[]
while index_1<len(my_list_1):
    my_result.append(my_list_1[index_1])
    index_1+=2
while index_2<len(my_list_2):
    my_result.append(my_list_2[юindex_2])
    index_2+=2
print(my_result)
##########################################

# 3b
for symbol in my_list_1:
    if not symbol%2:
        my_result.append(symbol)
for symbol in my_list_2:
    if symbol%2:
        my_result.append(symbol)
print(my_result)
###########################################

# 4
my_list=[1,2,3,4,5]
new_list=[]
index=1
while index<len(my_list):
    new_list.append(my_list[index])
    index+=1
new_list.append(my_list[0])
print(new_list)
###########################################

# 5
my_list.append(my_list[0])
my_list.pop(0)
print(my_list)
###########################################

# 6
my_str=input("Введи строку ")
my_list=my_str.split()
sum=0
for word in my_list:
    if word.isnumeric():
        sum+=int(word)
print("сумма чисел в строке ",sum)
###########################################

# 7
my_str=input("enter my_str ")
my_list=[]
for i in range(0,len(my_str),2):
    my_list.append(my_str[i:i+2])
if len(my_str)%2:
    my_list[-1]=my_list[-1]+"_"
print(my_list)
###########################################

# 8
my_str=input("enter my_str ")
l_limit=input("enter l_limit ")
r_limit=input("enter r_limit ")
sub_str=my_str[my_str.find(l_limit)+1:my_str.find(r_limit)]
print('sub_str => ',sub_str)
##########################################

# 9
sub_str=my_str[my_str.find(l_limit)+1:my_str.rfind(r_limit)]
print('sub_str => ',sub_str)
##########################################

# 10
my_list=list(map(int,input('Введите элементы списка через пробел ').split()))
# my_list=[int(symbol) for symbol in input('Введите элементы списка через пробел ').split()]
quantity=0
index=1
while index<len(my_list)-1:
    if int(my_list[index])>int(my_list[index-1])+int(my_list[index+1]):
        quantity+=1
    index+=1
print("количество искомых элементов = ",quantity)