import os
import random
import json

from my_tools import rand_string

# 1

with open('names.txt', 'r')as txt_file:
    data = []
    for line in txt_file.readlines():
        data.append(line.split()[1])
print(data)


##########################################

# 2

def dict_maker():
    my_dict = {}
    len_dict = random.randint(5, 20)
    for i in range(len_dict):
        my_dict[rand_string(5, 5)] = random.choice(
            [random.randint(-100, 100), random.random(), bool(random.getrandbits(1))])
        # bool(random.getrandbits(1)) - прочитал что так быстрее чем random.choice([True,False])
    return my_dict


#####################################

# 3

def generate_and_write_json(file_path):
    my_dict = dict_maker()
    with open(file_path, 'w') as js_file:
        json.dump(my_dict, js_file)


# generate_and_write_json('/Users/klema/PycharmProjects/Sobchenko_IntroPython_14_01/Sobchenko_IntroPython_14_01/test.json')
