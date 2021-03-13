import json
from pprint import pprint

# 1) Функция чтения из файла

def read_json(file_name):
  with open(file_name, 'r') as js_file:
     result = json.loads(js_file.read())
  return result
######################################

# 2) Сортировка по имени в алфавитном порядке

def sort_name():
    names = []
    list = read_json('Data.json')
    for dict in list:

        if " " in dict['name']: # Если в поле 'name' более одного слова-принимаю последнее за фамилию
            familia =  dict['name'][dict['name'].rfind(' ')+1:] # Это срез)
            names.append(familia)
        else: # Если в поле 'name' одно слово-оно и будет фамилией
            familia = dict['name']
            names.append(familia)

    names.sort()
    return names
print(sort_name())
########################################

# 3) Сортировка по дате смерти

def sort_date_death():
    death_list = []
    list = read_json('Data.json')
    for dict in list:
        # Годы до н.э. переведу в инт с отрицательным знаком для удобства сортировки
        if 'BC' in dict['years']:
            death_year = dict['years'][dict['years'].rfind(' ')-4:dict['years'].rfind(' ')] # Это срез)
            death_list.append({'name':dict['name'],'death in':-int(death_year)})

        else:
            death_year = dict['years'][dict['years'].rfind(' ')+1:dict['years'].rfind('.')]
            death_list.append({'name':dict['name'],'death in':int(death_year)})

    death_list = sorted(death_list, key=lambda x: x['death in'])
    # Верну отрицательным числам изначальный вид с "ВС"
    for dict in death_list:
        if dict['death in']<0:
            dict['death in'] = str(-dict['death in'])+" BC"
    return pprint(death_list) # Столбиком симпотичнее
print('######################################')
sort_date_death()

#############################################

# 4) Сортировка по количеству слов в поле "text"
def word_count():
    words_list = []
    list = read_json('Data.json')
    # Слова считаю из соображений что в любой стороке количество_слов=количество_пробелов+1
    words_list = [{'name':dict['name'],'words in "text"':dict['text'].count(' ')+1} for dict in list]
    words_list = sorted(words_list, key=lambda x: x['words in "text"'])
    return pprint(words_list)

print('#########################################')
word_count()