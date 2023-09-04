# Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.

def create_dictionary(**kvargs):

    result_dict = {}
    for values, key in kvargs.items():
        result_dict[str(key)] = values
    return result_dict

print(create_dictionary(first='hello, world', second=123, third=True))