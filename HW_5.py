# 2. Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os


def result_turp(path_file: str) -> tuple:
    head, tail = os.path.split(path_file)
    name_f, extension = tail.split('.')
    return head, name_f, extension


if __name__ == '__main__':
    abs_path = 'C:/Users/User/PycharmProjects/pythonProject/HW_5.py'
    print(f'Исходная строка {abs_path}\nКортеж из трех элементов {result_turp(abs_path)}')


# 3. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида “10.25%”.
# В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии


names = ['Mary', 'Garry', 'Beth']
salaries = [10000, 20000, 15000]
bonuses = ['10.25%', '12.25%', '15.50%']

dict_sum = {name: (salary * float(bonus[:-1])/100) for name, salary, bonus in zip(names, salaries, bonuses)}

print(dict_sum)


# 4. Создайте функцию генератор чисел Фибоначчи

def fib(size):
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


num = int(input('Введите количество чисел Фибоначчи: '))

fibonacci = iter(fib(num))

for _ in range(num):
    print(next(fibonacci))








