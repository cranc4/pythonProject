# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки
# препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.

word_list = []
result_dict = {}
sorted_dict = {}
word_top_size = 10
initial_line = '''В мире горы есть и долины есть,
В мире хоры есть и низины есть,
В мире море есть и лавины есть,
В мире боги есть и богини есть.'''.lower().replace(',', '').replace('.', '')

word_list = initial_line.split()

for i in word_list:
    if not i in result_dict.keys():
        result_dict[i] = word_list.count(i)

sorted_dict = dict(sorted(result_dict.items(), key=lambda item: item[1], reverse=True))

for i, word in enumerate(sorted_dict.items(), 1):
    if word_top_size == 0:
        break
    else:
        print(f'{i :> 3}. {word[0]} - {word[1]}')
        word_top_size -= 1