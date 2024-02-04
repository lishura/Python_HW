
'''
Задание №1
Вручную создайте список с целыми числами, которые повторяются. Получите новый список, который содержит уникальные (без повтора) элементы исходного списка.


*Подготовьте два решения, короткое и длинное, которое
не использует другие коллекции помимо списков.

'''
# my_list = [1,1,2,33,3,3,4,4,5,6,7]
# result = list(set(my_list))
#
# result_2 = []
# for item in my_list:
#     if not item in result_2:
#         result_2.append(item)
#
# print(f'{result = }')
# print(f'{result_2 = }')

'''
Задание №3
Пользователь вводит данные. Сделайте проверку данных
и преобразуйте если возможно в один из вариантов ниже:
Целое положительное число
Вещественное положительное или отрицательное число
Строку в нижнем регистре, если в строке есть
хотя бы одна заглавная буква
Строку в нижнем регистре в остальных случаях
'''

# text = input('Введите строку: ')
# if text.isdigit():
#     result = int(text)
# elif text.replace('.', "").replace("-", "").isdigit() and text.count('.') == 1 and text.count('-') <= 1 and '-' not in text[1:]:
#     result = float(text)
# elif not text.islower():
#     result = text.lower()
# else:
#     result = text.upper()
#
# print(f'{result=}')
# print(type(result))

# Задание №3 Создайте вручную кортеж содержащий элементы разных типов.
# Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

data = (42, 73, 3.14, 'Hello world!', None, True, 'Text', 100500.2, False)
result = {}
# for item in data:
#     key = type(item)
#     if key not in result:
#         value = [x for x in data if isinstance(x, type(item))]
#         result[key] = value
# print(f'{result = }')

# второй вариант решения

# for item in data:
#     key = result.setdefault(type(item), list())
#     key.append(item)
# print(f'{result = }')

# Задание №4
# Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.

# COUNT_DOUBL = 2
# data = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42]
#
# for item in set(data):
#     if data.count(item) == COUNT_DOUBL:
#         for _ in range(COUNT_DOUBL):
#             data.remove(item)
#
# print(data)


# Задание №5
# Создайте вручную список с повторяющимися целыми числами.
# Сформируйте список с порядковыми номерами
# нечётных элементов исходного списка.
# Нумерация начинается с единицы.

# data = [42, 73, 5, 42, 42, 2, 3, 5, 7, 73, 42]
#
# result = []
# for i in range(len(data)):
#     if data[i] % 2:
#         result.append(i + 1)
# print(result)
#
# result_2 = []
# for i, item in enumerate(data, 1):
#     if item % 2:
#         result_2.append(i)
# print(result_2)

# Задание №6
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# Строки нумеруются начиная с единицы.
# Слова выводятся отсортированными согласно кодировки Unicode.
# Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

# text = input('Введите текст: ').split()
# text.sort()
# # text = sorted(text)
# max_len = 0
# for item in text:
#     current_len = len(item)
#     if max_len < current_len:
#         max_len = current_len
#
# for i, item in enumerate(text, start = 1):
#     print(f'{i}. {item:>{max_len}}')

# Задание №7
# Пользователь вводит строку текста.
# Подсчитайте сколько раз встречается
# каждая буква в строке без использования
# метода count и с ним.
# Результат сохраните в словаре, где ключ — символ, а значение — частота встречи
# символа в строке.
# Обратите внимание на порядок ключей. Объясните почему они совпадают
# или не совпадают в ваших решениях.

# text = 'assadfsfgdfjwes'
# result = {}
# for char in set(text):
#     result[char] = text.count(char)
# print(f'{result = }')
#
# result_2 = {}
# for char in text:
# # if char in result_2:
# # result_2[char] += 1
# # else:
# # result_2[char] = 1
#     result_2[char] = result_2.get(char, 0) + 1
# print(f'{result_2 = }')

# Задание №8 Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# Какие вещи взяли все три друга
# Какие вещи уникальны, есть только у одного друга
# Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

# hike = {
# 'Aaz': ("спички", "спальник", "дрова", "топор"),
# 'Skeeve': ("спальник", "спички", "вода", "еда"),
# 'Tananda': ("вода", "спички", "косметичка"),
# }
# all_things = set()
# for values in hike.values():
#     all_things.update(values)
#
# print(f'{all_things = }')
#
# things_all_friends = list(hike.values())
# things_first_friend = things_all_friends[0]
# thigs_other_friends = things_all_friends[1:]
# print(things_all_friends)
# print(things_first_friend)
# print(thigs_other_friends)
# for thing in things_first_friend:
#     all_friends = True
#     for things in thigs_other_friends:
#         if thing not in things:
#             all_friends = False
# if all_friends:
#     print(f'Вещь {thing} есть у всех 3 друзей')
#
# unique = {}
#
# for master_key, master_value in hike.items():
#     for slave_key, slave_value in hike.items():
#         if master_key != slave_key:
#             if not unique.get(master_key):
#                 unique[master_key] = set(master_value) - set(slave_value)
#             else:
#                 unique[master_key] -= set(slave_value)
# print(unique)
#
# dublicates = all_things
# for things in unique.values():
#     dublicates -= things
# print(f'{dublicates=}')
#
# for key, value in hike.items():
#     result = dublicates-set(value)
#     if result:
#         print(f'У {key} отсуствует {result}')



