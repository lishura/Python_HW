
# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
#
# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные варианты и выведите 4 успешных расстановки.

import random

__all__ = ['is_queen_beat', 'position_generation']


QUEENS_NUMBER = 8


def is_queen_beat(position: list[list[int]]) -> bool:

    x = []
    y = []

    for i in range(QUEENS_NUMBER):
        x.append(position[i][0])
        y.append(position[i][1])
    correct = True
    for i in range(QUEENS_NUMBER):
        for j in range(i + 1, QUEENS_NUMBER):
            if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
                correct = False
    if correct:
        return True  # ферзи не бьют друг друга
    else:
        return False  # ферзи бьют друг друга


def position_generation():
    position = []
    n = QUEENS_NUMBER
    i = 0
    while i < n:
        x = random.randint(1, 9)
        y = random.randint(1, 9)
        if [x, y] not in position:
            position.append([x, y])
            i += 1
    return position

