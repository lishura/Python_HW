# Задание №6 Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

# BIG_LEAP_YEAR = 400
# LARGE_NOT_BIG_YEAR = 100
# SMALL_LEAP_YEAR = 4
# REFORM = 1582
#
# year = int(input('Введите год: '))
#
# if year < REFORM:
#     result = f'Год {year} до введения Григорианского календаря'
# elif not year % BIG_LEAP_YEAR:
#     result = f'Год {year} високосный'
# elif not year % LARGE_NOT_BIG_YEAR:
#     result = f'Год {year} не високосный'
# elif not year % SMALL_LEAP_YEAR:
#     result = f'Год {year} високосный'
# else:
#     result = f'Год {year} не високосный'
#
# print(result)

# Задание №7
# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

# LOWER_LIMIT = 1
# UPPER_LIMIT = 999
# TEN = 10
# HUNDRED = 100
# number = LOWER_LIMIT - 1
#
# while number < LOWER_LIMIT or number > UPPER_LIMIT:
#     number = int(input(f'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}: '))
#
# if number < TEN:
#     result = f'Число {number} - цифра. Ее квадрат равен {number * number}.'
# elif number < HUNDRED:
#     result = f'Число {number} - двузначное. Произведение его цифр равно {(number // TEN) * (number % TEN)}.'
# else:
#     result = f'Число {number} - трехзначное. Его зеркальное отображение {(number % TEN)}{number // TEN % TEN}{number // HUNDRED}.'
# print(result)

# Задание №9 Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.

# LOWER_LIMIT = 2
# UPPER_LIMIT = 11
# COLUMNS = 4
#
# for row in (LOWER_LIMIT, LOWER_LIMIT + COLUMNS):
#     for num_2 in range(LOWER_LIMIT, UPPER_LIMIT):
#         for num_1 in range(row, row + COLUMNS):
#             print(f'{num_1:>2} x {num_2:>2} = {num_1 * num_2:>2}', end='\t')
#         print()
#     print()

# Задание №8 Нарисовать в консоли ёлку спросив
# у пользователя количество рядов.
# Пример результата:
# Сколько рядов у ёлки? 5
#     *
#    ***
#   *****
#  *******
# *********

# SPACE = ' '
# STAR = '*'
# ONE = 1
# rows = int(input('Сколько рядов у елки? '))
# spaces = rows - ONE
# stars = ONE
#
# for _ in range(rows):
#     print(spaces * SPACE + stars * STAR)
#     spaces -= 1
#     stars += 2
