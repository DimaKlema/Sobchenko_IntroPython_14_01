import random as rnd
import string

# Переделал согласно вашим замечаниям:
#   В первом задании собрал возврат в функции с помощью f-строки
#   В третьем задании разбил на отдельные функции

names = ['armstrong', 'oldrin', 'mitchel', 'scott']
domains = ['net', 'com', 'ua', 'ru']


def create_email(domains, names):
    rand_str = ''.join(rnd.choice(string.ascii_lowercase) for i in range(rnd.randint(5, 7)))
    # return rnd.choice(names) + '.' + str(rnd.randint(100, 999)) + '@' + str(rand_str) + '.' + rnd.choice(domains)
    return f"{rnd.choice(names)}.{str(rnd.randint(100, 999))}@{str(rand_str)}.{rnd.choice(domains)}"


e_mail = create_email(domains, names)
print(e_mail)

###########################################

# 2
def rand_len_str(min_limit, max_limit):
    return ''.join(rnd.choice(string.ascii_letters + string.digits) for i in range(rnd.randint(min_limit, max_limit)))


my_str = rand_len_str(40, 70)
print(my_str)

##############################################################


# 3
# Чтоб придать реалистичности тексту, я провёл такое иследование:
#   1. Взял текст с первых трёх страниц "Войны и мир". Посчитал в этом тексте пробелы, знаки препинания и
#      заглавные буквы.
#   2. В среднем на каждые 4 слова приходится 1-о с заглавной буквой.
#   3. Получилось что на 8 пробелов приходится 2 запятые, 1 тире и 1 двоеточие. Поэтому в списке punct_symb, из
#      которого я буду случайно выбирать знаки препинания, эти знаки препинания находятся в количественном
#      отношении друг к другу так: пробел/запятая/двоеточие/тире = 8/2/1/1
#      В взятом тексте двоеточий и тире больше чем в каком либо другом, потому что на балу у Анны Павловны
#      было много прямой речи =)
#  Я выдержал эти пропорции и поэтому можно сказать что функция sentence_generator преобразует строку
#  в текст in Толстой style  =)

def sort_string(my_str): # сортирует строку на буквы и цифры
    letters = ''
    numbers = ''
    for symbol in my_str:
        if symbol.isnumeric():
            numbers += symbol
        else:
            letters += symbol
    return letters,numbers

##########################

def break_string(letters,numbers):  # разбиваet строку букв на слова случайной длины от 1 до 10
    i = 0
    words = ''
    while i <= len(letters):
        a = rnd.randint(1, 10)
        word = (letters[i:i + a] + ' ')
        words += word
        i += a

    words_new = words.rstrip().capitalize()  # удаляю последний пробел и делаю заглавной первую букву
    word_list = words_new.split(' ')  # перехожу к списку для удобства
    word_list.insert(rnd.randint(1, len(word_list)), numbers)  # возвращаю на случайное место отобранные вначале цифры
    return word_list

##########################


def capital_letter(word_list):   # делаet заглавные буквы в словах так чтоб их было не больше чем одно слово из четырёх
    i = 1
    while i <= len(
            word_list[1:]) // 4:
        a = rnd.randint(i, i + 4)
        word_list[a] = word_list[a].title()
        i += 1
    return word_list

##########################

def words_marks_collector(word_list):   # собираet до кучи слова, пробелы и знаки препинания
    end = ['!', '?', '!!!', '?!', '.', '...']
    punct_symb = [', ', ', ', ': ', ' - ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' \\n ']
    sentence = []

    for word in word_list:
        sentence.append(word)
        sentence.append(rnd.choice(punct_symb))

    if sentence[-1] in punct_symb:  # случайно выбираю конечный знак
        del sentence[-1]
        sentence.append(rnd.choice(end))
    else:
        sentence.append(rnd.choice(end))
    return sentence

##########################

def sentence_generator(my_str): # а теперь всё вместе
   letters,numbers = sort_string(my_str)
   sentence = words_marks_collector(capital_letter(break_string(letters,numbers)))
   return ''.join(sentence)

print(sentence_generator(my_str))