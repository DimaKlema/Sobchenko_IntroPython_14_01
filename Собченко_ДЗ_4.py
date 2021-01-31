# 1
my_list=[1,34,555,124,56]
my_result=[]
for symbol in my_list:
    if symbol>100:
        print(symbol)
##################################

# 2
for symbol in my_list:
    if symbol>100:
        my_result.append(symbol)
print(my_result)
##################################

# 3
my_list.append(0) if len(my_list)<2 else my_list.append(my_list[-1]+my_list[-2])
##################################

# 5
my_indexes=[0,1,2,3,4]
for index in my_indexes :
    print(my_list[index])
###################################

# 6
my_list_1=[1,2,3,4,5]
my_list_2=[6,7,8,9,0]
for index in my_indexes:
    print(my_list_1[index], my_list_2[index])
####################################

#7
my_string='0123456789'
integer_list=[]
for symb_1 in my_string:
    for symb_2 in my_string:
        integer_list.append(int(symb_1 + symb_2))
print(integer_list)