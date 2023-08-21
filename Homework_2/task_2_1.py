# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйтe для проверки своего результата.

def recalculation_number_system(number):
    string_to_translate = '0123456789ABCDEF'
    result = ''
    notation = 16

    while number > 0:
        result = string_to_translate[number % notation] + result
        number //= notation

    return result

print(recalculation_number_system(int(input('Введите число для перевода в 16-ю систему счисления: '))))