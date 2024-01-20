# 1. Напишите функцию для транспонирования матрицы


my_matrix = [[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 0]]


def transposing(matrix):
    matrix_t = [[0 for j in range(len(matrix))] for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix_t[j][i] = matrix[i][j]
    return matrix_t


print(transposing(my_matrix))


# 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.


def func(**kwargs):
    result = {}
    for key, value in kwargs.items():
        result[value] = key
    return result


print(func(name='Alexandra', surname='Lisovskaya'))


# 3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

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
CMD_TOP_UP = "1"
CMD_WITHDRAW = "2"
CMD_EXIT = "3"

balance = 0
operations = 0
list_operations = []


def check_cash():
    while True:
        cash = int(input("Введите сумму опреации кратно 50: \n"))
        if cash % 50 == 0:
            return cash


def top_up_balance(cash):
    global balance
    global operations
    global list_operations
    balance += cash
    print(f'Баланс Вашей карты {balance}')
    operations += 1
    if operations % 3 == 0:
        balance = balance + PERCENT_BONUS * balance
        print(f'Вам начислены проценты в сумме {PERCENT_BONUS * balance}')
    list_operations.append([(f'пополнение {cash}')])

def withdraw(cash):
    global balance
    global operations
    global list_operations
    comission = cash * PERCENT
    if comission < MIN_LIMIT:
        comission = MIN_LIMIT
    elif comission > MAX_LIMIT:
        comission = MAX_LIMIT
    if comission + cash > balance:
        print("На балансе недостаточно средств")
    else:
        balance -= (cash + comission)
        print(f"Сумма снятия {cash}, комиссия {comission}, баланс вашей карты {balance}")
        operations += 1
        if operations % 3 == 0:
            balance = balance + PERCENT_BONUS * balance
            print(f'Вам начислены проценты в сумме {PERCENT_BONUS * balance}')
    list_operations.append([(f'снятие {cash}')])


def cmd_exit():
    global list_operations
    print('Будем рады видеть Вас снова!\n')
    print('Список операций: ')
    for item in list_operations:
        print(*item)
    exit()


def richness():
    global balance
    if balance > RICHNESS_AMOUNT:
        sum_percent = balance * PERCENT_RICHNESS
        balance -= sum_percent
        print(f"Вычтен налог на богатство в размере {sum_percent}")
        print(f"Текущий баланс {balance}")


while True:
    action = int(input(
        f"пополнить-{CMD_TOP_UP}\n"
        f"снять-{CMD_WITHDRAW}\n"
        f"выход-{CMD_EXIT}\n"
        f"Введите действие: "
    ))
    if action == 1:
        richness()
        top_up_balance(check_cash())

    elif action == 2:
        richness()
        withdraw(check_cash())

    else:
        richness()
        cmd_exit()




