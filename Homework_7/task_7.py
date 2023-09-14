# Напишите функцию группового переименования файлов. Она должна:
#  принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
#  принимать параметр количество цифр в порядковом номере.
#  принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
#  принимать параметр расширение конечного файла.
#  принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.

import os
from random import sample
from string import ascii_letters

def rename_files(end_name, digits, source_extension, dest_extension, name_range=(0, -1)):
    files = os.listdir(os.path.join(os.getcwd(), 'new_folder'))

    filtered_files = [f for f in files if f.endswith(source_extension)]

    for i, file in enumerate(filtered_files, 1):
        old_name = os.path.splitext(file)[0][name_range[0]:name_range[1]]

        new_name = f"{old_name}_{end_name}_{str(i).zfill(digits)}{dest_extension}"

        old_path = os.path.join(os.getcwd(), 'new_folder', file)
        new_path = os.path.join(os.getcwd(), 'new_folder', new_name)
        os.rename(old_path, new_path)


def creating_demo_folder(number_files: int, extension: str):
    os.mkdir('new_folder')

    for _ in range(number_files):
        file_name = ''.join(sample(ascii_letters, 5)) + extension
        demo_path = os.path.join(os.getcwd(), 'new_folder', file_name)

        with open(demo_path, 'w'):
            continue


creating_demo_folder(7, '.txt')

rename_files('new', 2, '.txt', '.doc', (1, 5))