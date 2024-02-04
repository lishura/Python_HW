# a = 5
# b = 0.5
# c = "text"
# d = (1,2)
# e = [4,5,6,7]
#
# print(f' Объект {a} имеет тип {type(a)}')
# print(f' Объект {b} имеет тип {type(b)}')
# print(f' Объект {c} имеет тип {type(c)}')
# print(f' Объект {d} имеет тип {type(d)}')
# print(f' Объект {e} имеет тип {type(e)}')

# Задание №2
# Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
# порядковый номер начиная с единицы
# значение
# адрес в памяти
# размер в памяти
# хэш объекта
# результат проверки на целое число только если он положительный
# результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.

# data = [42, 73.0, 'Hello world!', True, 42, 'Hello world!', 256, 2 ** 8, 1, 'Привет, мир!']
#
# for i, item in enumerate(data, start=1):
#     print(f'{i} значение {item}, адрес {id(item)}, размер {item.__sizeof__()}, хэш {hash(item)}')
#     if isinstance(item, int):
#         print("Это целое число")
#     elif isinstance(item, str):
#         print("Это строка")
#     print()

# Задание №3
# Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно

# DIV_BIN = 2
# DIV_OCT = 8
#
# original_num: int = int(input("Введите целое число "))
# for div in (DIV_BIN, DIV_OCT):
#     num = original_num
#     result: str = ''
#     while num > 0:
#         result = str(num % div) + result
#         num //= div
#     print(f'Число {original_num} в {div} системе {result}')

# Задание №4
# Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# Диаметр не превышает 1000 у.е.
# Точность вычислений должна составлять
# не менее 42 знаков после запятой.

# from math import pi
# import decimal
#
# decimal.getcontext().prec = 42
# PI = decimal.Decimal(pi)
# diameter = decimal.Decimal(input("Введите диаметр: "))
# while diameter > 1000:
#     print("Диаметр не должен быть больше 1000")
#     diameter = decimal.Decimal(input("Введите диаметр: "))
# sqaure = PI * (diameter / 2) ** 2
# length = PI * diameter
# print(f"Площадь равна {sqaure}\nДлина равна {length}")

# Задание №5
# Напишите программу, которая решает квадратные уравнения даже если
# дискриминант отрицательный.
# Используйте комплексные числа
# для извлечения квадратного корня.

# from random import uniform
#
# a = uniform(-100, 100)
# b = uniform(-100, 100)
# c = uniform(-100, 100)
#
# print(f'{a}x^2 + {b}x + {c} = 0')
# d = b ** 2 - 4 * a * c
# print(f'{d=}')
# if d > 0:
#     x1 = (-b + d ** 0.5)/(2*a)
#     x2 = (-b - d ** 0.5)/(2*a)
#     result = f'Уравнение имеет два корня {x1= }, {x2= }'
# elif d == 0:
#     x = -b / (2 * a)
#     result = f'Уравнение имеет один корень {x= }'
# else:
#     d = complex(d, 0)
#     x1 = (-b + d ** 0.5) / (2 * a)
#     x2 = (-b - d ** 0.5) / (2 * a)
#     result = f'Уравнение имеет два комплексных корня {x1= }, {x2= }'
#
# print(result)

# Задание №6
# Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

import decimal

decimal.getcontext().prec = 2
MULTIPLICITY = 50
PERCENT = decimal.Decimal(15) / decimal.Decimal(1000)
PERCENT_BONUS = decimal.Decimal(3) / decimal.Decimal(100)
COUNT_PERC = 3
MIN_LIMIT = decimal.Decimal(30)
MAX_LIMIT = decimal.Decimal(600)
PERCENT_RICHNESS = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_AMOUNT = 5_000_000
CMD_DEPOSIT = "1"
CMD_WITHDRAW = "2"
CMD_EXIT = "3"

balance = 0
operations = 0

while True:
    action = input(
        f"пополнить-{CMD_DEPOSIT}\n"
        f"снять-{CMD_WITHDRAW}\n"
        f"выход-{CMD_EXIT}\n"
        f"Введите действие: "
    )
    if balance > RICHNESS_AMOUNT and action != "3":
        sum_percent = balance * PERCENT_RICHNESS
        balance -= sum_percent
        print(f"Вычтен налог на богатство в размере {sum_percent}")
        print(f"Текущий баланс {balance}")
    if action == "1" or action == "2":
        amount = 1
        while amount % MULTIPLICITY != 0:
            amount = int(input(f"Введите сумму кратную {MULTIPLICITY}: "))
        if action == "1":
            operations += 1
            balance += amount
        else:
            comission = amount * PERCENT
            if comission < MIN_LIMIT:
                comission = MIN_LIMIT
            elif comission > MAX_LIMIT:
                comission = MAX_LIMIT
            if comission + amount > balance:
                print("На балансе недостаточно средств")
            else:
                operations += 1
                balance -= (amount + comission)
            print(f"Сумма снятия {amount}, комиссия {comission}, общая сумма {amount + comission}")
    # print(f"Текущий баланс {balance}")
        if operations % COUNT_PERC == 0:
            bonus_sum = balance * PERCENT_BONUS
            balance += bonus_sum
            print(f"Сумма бонуса {bonus_sum}")
        # print(f"Текущий баланс {balance}")
            print(f"Текущий баланс {balance}")
    elif action == "3":
        break
    else:
        print("Введена неверная команда")


