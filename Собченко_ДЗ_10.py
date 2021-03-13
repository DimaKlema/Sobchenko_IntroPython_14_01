from pathlib import Path
import json
import csv
import os


def read_file(path_file):
    # filename, extension_file = os.path.splitext(file_path) # решил решить без сторонних библиотек
    extension_file = path_file[path_file.rfind('.'):]

    if extension_file == '.txt':
        with open(path_file, 'r') as txt_file:
            result = txt_file.read()
            return result

    elif extension_file == '.json':
        with open(path_file, 'r') as js_file:
            result = json.loads(js_file.read())
            return json.dumps(result, indent=1)  # возвращаю результат столбиком для удобства

    elif extension_file == '.csv':
        with open(path_file) as csv_file:
            temporary = csv.reader(csv_file)
            result = [row for row in temporary]
            return ('\n'.join(str(line) for line in result))  # возвращаю результат столбиком для удобства
    else:
        print("Unsupported file format")


path_file = input()
# print(read_file(file_path))

# /Users/klema/PycharmProjects/Sobchenko_IntroPython_14_01/Sobchenko_IntroPython_14_01/my_group.csv
# /Users/klema/PycharmProjects/Sobchenko_IntroPython_14_01/Sobchenko_IntroPython_14_01/names.txt
# /Users/klema/PycharmProjects/Sobchenko_IntroPython_14_01/Sobchenko_IntroPython_14_01/test.json

data = 'Сатья Наделла     12  1200'
# data = {'Сата Наделла':1200}


def write_file(path_file, data):
    extension_file = path_file[path_file.rfind('.'):]
    print(extension_file)
    if extension_file == '.txt':
        with open(path_file, 'a') as txt_file:
            result = txt_file.writelines('\n') # добавляю данные с новой строки для понятности
            result = txt_file.writelines(data)
            return result

    elif extension_file == '.json':
        with open(path_file, 'a') as js_file:
            return json.dump(json.loads(data.replace(' ')),js_file)

    elif extension_file == '.csv':
        with open(path_file, "a") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(data.split())

            # for row in data:
            #     writer.writerow(row)


print(write_file(path_file, data))
