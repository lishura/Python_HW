# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
# Дано a, b, c - стороны предполагаемого треугольника.
# Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
# Если хотя бы в одном случае отрезок окажется больше суммы двух других,
# то треугольника с такими сторонами не существует.
# Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.


# from random import uniform
#
# a = round(uniform(0, 1000), 2)
# b = round(uniform(0, 1000), 2)
# c = round(uniform(0, 1000), 2)
#
# print (f'Проверяем треугольник со сторонами {a=}, {b=}, {c=}.')
#
# if a < (b + c) and b < (a + c) and c < (a + b):
#     print('Такой треугольник существует.')
#     if a == b == c:
#         print('И он является равносторонним.')
#     elif a == b or a == c or b == c:
#         print('И он является равнобедренным.')
#     else:
#         print('И он является разносторонним.')
# else:
#     print('Такой треугольник не существует.')


# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.


# count = 0
#
# while True:
#     num = int(input('Введите целое число от 0 до 100 000: '))
#     if num >= 0 and num <= 100_000:
#         for i in range(2, num//2 + 1):
#             if num % i == 0:
#                 count += 1
#         if count > 0:
#             print(f'Число {num} составное')
#         else:
#             print(f'Число {num} простое')
#         break
#     else:
#         print("Введена неверное число")


# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
rand_num = randint(LOWER_LIMIT, UPPER_LIMIT)

attempt = 10

for _ in range (0, attempt):
    num = int(input(f'Угадайте целое число от {LOWER_LIMIT} до {UPPER_LIMIT}. Осталось {attempt} попыток. Введите число: '))
    if num == rand_num:
        print(f'Ура! Вы угадали! Загаданное число {rand_num}')
        break
    elif num < rand_num:
        print('Не угадали. Загаданное число больше.')
        attempt -= 1
    else:
        print('Не угадали. Загаданное число меньше.')
        attempt -= 1
        if attempt == 0:
            print('Сожалеем. Количество попыток истекло.')



