# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла. Функция возвращает кортеж из
# трёх элементов: путь, имя файла, расширение файла.

import os

def parse_path(path_file:str) -> tuple:
    *path, name = path_file.split('\\')
    result = ['/'.join(path), name.split('.')[0], name.split('.')[1]]
    return tuple(result)


path_to_file = os.path.abspath('task5_1.py')
print(parse_path(path_to_file))