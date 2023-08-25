# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

from random import randint as ran

initial_list = [ran(1,10) for i in range(10)]
result_list = []

for number in initial_list:
    if initial_list.count(number) >= 2 and number not in result_list:
        result_list.append(number)

print(f'{initial_list = }\n{result_list =}')