# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = [3,8,9,3,2,8,3,5,9,1,1,7,'a','a','b','a']
result = []

for item in my_list:
    if my_list.count(item) > 1:
        result.append(item)
print(set(result))


# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов. За основу возьмите любую статью из википедии
# или из документации к языку.

COUNT_MAX_FREQUENCY = 10

my_text = 'В мире горы есть и долины есть, ' \
          'В мире хоры есть и низины есть, ' \
          'В мире море есть и лавины есть, ' \
          'В мире боги есть и богини есть.'

my_text = my_text.replace(',','').replace('.','').replace('!','').replace('?','').replace('-','')
my_text = my_text.lower().split()
frequency_dict = {}

for word in my_text:
    frequency_dict.setdefault(word, my_text.count(word))

count_words = 1

while count_words <= COUNT_MAX_FREQUENCY:
    count_words += 1
    max_key = max(frequency_dict, key=frequency_dict.get)
    print(f'{max_key:>5} = {frequency_dict[max_key]}')
    frequency_dict.pop(max_key)


# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.

things = {'спальник': 3, 'палатка': 10, 'котелок': 1, 'еда': 8, 'посуда': 4, 'одежда': 3, 'вода': 10}

max_carrying = int(input('Введите максимальную грузоподъемность рюкзака: '))
possible_things = []
for thing, weight in things.items():
    if weight <= max_carrying:
        possible_things.append(thing)
        max_carrying -= weight
print(f'В такой рюкзак может влезть {possible_things}')








