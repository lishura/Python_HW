# Задание №1
# Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.
#
# Сформируйте словарь, где:
# второе и третье число являются ключами.
# первое число является значением для первого ключа.
# четвертое и все возможные последующие числа
# хранятся в кортеже как значения второго ключа.

# text = input("Введите числа через '/': ")
# first, second, third, *other = text.split('/')
# result = {int(second): int(first), int(third): tuple(map(int, other))}
# print(result)

# Задание №2
# Самостоятельно сохраните в переменной строку текста.
# Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# Напишите преобразование в одну строку.

# text = 'asafsgfdgssds'
# result = {char: ord(char) for char in text}
# print(result)

# Задание №3
# Продолжаем развивать задачу 2.
# Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.

# data = iter(result.items())
# for _ in range(5):
#     print(next(data))


# Задание №4
# Создайте генератор чётных чисел от нуля до 100.
# Из последовательности исключите
# числа, сумма цифр которых равна 8.
# Решение в одну строку.

# my_gen = (num for num in range(0, 101, 2) if num // 10 + num % 10 != 8)
# print(*my_gen)

# Задание №5
# Напишите программу, которая выводит
# на экран числа от 1 до 100.
# При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# Вместо чисел, кратных пяти — слово «Buzz».
# Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# *Превратите решение в генераторное выражение.

# for num in range(1, 101):
#     result = ''
#     if not num % 15:
#         result = "FizzBuzz"
#     elif not num % 5:
#         result = "Buzz"
#     elif not num % 3:
#         result = "Fizz"
#     else:
#         result = str(num)
#     print(result)
#
# final_result = ("FizzBuzz" if not num % 15
#                 else "Buzz" if not num % 5
#                 else "Fizz" if not num % 3
#                 else num for num in range(1, 101)
#                 )
# print(*final_result)


# Задание №6
# Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# Таблицу создайте в виде однострочного генератора, где каждый элемент генератора — отдельный пример таблицы умножения.
# Для вывода результата используйте «принт»
# без перехода на новую строку.

# LOWER_LIMIT = 2
# UPPER_LIMIT = 11
# COLUMNS = 4
# for row in (LOWER_LIMIT, LOWER_LIMIT + COLUMNS):
#     for num_2 in range(LOWER_LIMIT, UPPER_LIMIT):
#         for num_1 in range(row, row + COLUMNS):
#             print(f'{num_1:>2} X {num_2:>2} = {num_1 * num_2:>2}', end='\t')
#         print()
#     print()

# my_gen = ("\n\n".join(["\n".join([" ".join([f'{num_1:>2} X {num_2:>2} = {num_1 * num_2:>2}'
# for num_1 in range(row, row + COLUMNS)])
# for num_2 in range(LOWER_LIMIT, UPPER_LIMIT)])
# for row in (LOWER_LIMIT, LOWER_LIMIT + COLUMNS)]))
# print(*my_gen)

# my_gen = (
#             f'{num_1:>2} X {num_2:>2} = {num_1 * num_2:>2}\t'
#             if num_1 != row + COLUMNS - 1 else f'{num_1:>2} X {num_2:>2} = {num_1 * num_2:>2}\n'
#             if num_2 != UPPER_LIMIT -1 else f'{num_1:>2} X {num_2:>2} = {num_1 * num_2:>2}\n\n'
#             for row in (LOWER_LIMIT, LOWER_LIMIT + COLUMNS)
#             for num_2 in range(LOWER_LIMIT, UPPER_LIMIT)
#             for num_1 in range(row, row + COLUMNS)
#             )
# print(*my_gen)


# Задание №7
# Создайте функцию-генератор.
# Функция генерирует N простых чисел,
# начиная с числа 2.
# Для проверки числа на простоту используйте правило:
# «число является простым, если делится нацело только на единицу и на себя».

def prime_number_gen(limit):
    yield 2
    number = 3
    while limit - 1:
        for div in range(3, int(number ** 0.5) + 1, 2):
            if not number % div:
                break
        else:
            yield number
            limit -= 1
        number += 2


for item in prime_number_gen(10):
    print(item)


