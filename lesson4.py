# Задание №1
# Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# Строки нумеруются начиная с единицы.
# Слова выводятся отсортированными согласно кодировки Unicode.
# Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.


def func(text: str) -> None:
    result = sorted(text.split())
    max_length = len(max(result, key=len))
    for i, item in enumerate(result,1):
        print(f'{i}. {item:>{max_length}}')


func("раз два три четыре пятьдесятсемь")

# Задание №2 Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.


def func(text:str)->list[int]:
    result = set()
    for char in text:
        result.add(ord(char))
    return sorted(result, reverse=True)

print(func("asdfghjkdfg"))

# Задание №3
# Функция получает на вход строку из двух чисел через пробел.
# Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.


def func(text: str) -> dict[str, int]:
    nums = list(map(int, text.split()))
    result = {chr(num): num for num in range(min(nums), max(nums) + 1)}
    return result

print(func("76 67"))

# Задание №4
# Функция получает на вход список чисел.
# Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

def func(lst:list[int]):
    cnt = 1
    while cnt < len(lst):
        is_sorted = True
        for i in range(len(lst) - cnt):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                is_sorted = False
        if is_sorted:
            break
        cnt += 1


lst_sorted = [8,99,4,5,6,88,74,52]
func(lst_sorted)
print(lst_sorted)


# Задание №5 Функция принимает на вход три списка одинаковой длины:
# имена str,
# ставка int,
# премия str с указанием процентов вида «10.25%».
# Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.

def func(names: list[str], salary: list[int], bonus: list[str]) -> dict[str, float]:
    result = {name: salary * float(bonus[:-1]) / 100
              for name, salary, bonus in zip(names, salary, bonus)}
    return result


n = ["Иван", "Николай", "Пётр", "Харитон"]
s = [125_000, 96_000, 109_000, 100_000]
a = ['10%', '25.5%', '13.3%', '42.73%']

print(func(n, s, a))


# Задание №6
# Функция получает на вход список чисел и два индекса.
# Вернуть сумму чисел между между переданными индексами.
# Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.

def func(nums: list[int], first: int, second: int):
    min_idx = max(min(first, second), 0)
    max_idx = min(max(first, second), len(nums))
    result = sum(nums[min_idx+1:max_idx])
    return result


print(func([1, 4, 5, 6, 8, 9, 11], 5, 2))

# Задание №7 Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# Вычислите итоговую прибыль или убыток каждой компании. Если все компании прибыльные,
# верните истину, а если хотя бы одна убыточная — ложь.

data = {
"Рога": [42, 73, 12, 85, -15, 2],
"Копыта": [45, 25, 100, 22, 1],
"Хвосты": [-500, 123, 52, 45, 93],
}

def func(data: dict[str, list[int]]):
# for value in data.values():
#   if sum(value) < 0:
#       return False
#   return True
    return all(map(lambda x: sum(x) > 0, data.values()))
    # return len(list(filter(lambda x: sum(x) > 0, data.values()))) == len(data)

print(func(data))


# Задание №8
# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s
# (кроме переменной из одной буквы s) на None.
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

datas = [42, -73, 12, 85, -15, 2]
s = 'Hello world!'
names = ('NoName', 'OtherName', 'NewName')
sx = 42

def func():
    data = globals()
    for var, value in data.copy().items():
        if var.endswith("s") and len(var) > 1:
            data[var[:-1]] = value
            data[var] = None


func()
print(f'{datas = }')
print(f'{s = }')
print(f'{names = }')
print(f'{sx = }')
print(f"{data = }")
print(f'{name = }')