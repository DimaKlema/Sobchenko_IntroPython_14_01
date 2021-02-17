import random as rnd
import string

# 1 в генерации строки использую только нижний регистр. В условии об етом не сказано,
#    но комбинировать верхний регистр с нижним в имени почтового ящика врядли нужно
names = ['armstrong', 'oldrin', 'mitchel', 'scott']
domains = ['net', 'com', 'ua', 'ru']


def create_email(domains, names):
    rand_str = ''.join(rnd.choice(string.ascii_lowercase) for i in range(rnd.randint(5, 7)))
    return rnd.choice(names) + '.' + str(rnd.randint(100, 999)) + '@' + str(rand_str) + '.' + rnd.choice(domains)


e_mail = create_email(domains, names)
print(e_mail)


###########################################

# 2
def rand_len_str(min_limit, max_limit):
    return ''.join(rnd.choice(string.ascii_letters + string.digits) for i in range(rnd.randint(min_limit, max_limit)))


my_str = rand_len_str(40, 70)
print(my_str)

############################################

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
def sentence_generator(my_str):
   word_list=[]
   punct_symb=[', ',', ',': ',' - ',' ',' ',' ',' ',' ',' ',' ',' ',' \\n ']
   letters=''
   numbers=''
   for symbol in my_str:  # сортирую строку на буквы и цифры
       if symbol.isnumeric():
         numbers+=symbol
       else:
         letters+=symbol

   i=0
   words=''
   while i<=len(letters): # разбиваю строку букв на слова случайной длины от 1 до 10
      a = rnd.randint(1, 10)
      word=(letters[i:i+a]+' ')
      words+=word
      i+=a

   words_1=words.rstrip().capitalize()# удаляю последний пробел и делаю заглавной первую букву
   word_list=words_1.split(' ')# перехожу к списку для удобства
   word_list.insert(rnd.randint(1,len(word_list)),numbers) # возвращаю на случайное место отобранные вначале цифры

   i=1
   while i<=len(word_list[1:])//4:# делаю заглавные буквы в словах так чтоб их было не больше чем одно слово из четырёх
       a=rnd.randint(i,i+4)
       word_list[a]=word_list[a].title()
       i+=1

   sentence = []
   for word in word_list: # собираю до кучи слова, пробелы и знаки препинания
       sentence.append(word)
       sentence.append(rnd.choice(punct_symb))

   end=['!', '?', '!!!', '?!', '.', '...']
   if sentence[-1] in punct_symb: # случайно выбираю конечный знак
       del sentence[-1]
       sentence.append(rnd.choice(end))
   else:
       sentence.append(rnd.choice(end))
   return ''.join(sentence)

print(sentence_generator(my_str))