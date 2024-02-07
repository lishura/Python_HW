# Задание №1
# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции.

from random import randint, uniform
from pathlib import Path

__all__ = ['write_file', 'gen_names', 'read_or_begin', 'sum_files', 'gen_files', 'num_files', 'gen_different_files',
           'sort_files']

MIN_NUM = -1000
MAX_NUM = 1000


def write_file(num_str: int, f_name: Path) -> None:
    with open(f_name, 'w', encoding='UTF-8') as f:
        for _ in range(num_str):
            f.write(f'{randint(MIN_NUM, MAX_NUM)} | {uniform(MIN_NUM, MAX_NUM)}\n')


if __name__ == '__main__':
    write_file(10, Path('numbers.txt'))

# Задание №2 Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# Полученные имена сохраните в файл.

from random import randint, choice
from pathlib import Path

MIN_VALUE = 4
MAX_VALUE = 7
VOWELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'


def gen_names(str_counts: int, file_name: Path) -> None:
    with open(file_name, "a", encoding="UTF-8") as f:
        for _ in range(str_counts):
            name = ''
            flag = choice([-1, 1])
            for _ in range(randint(MIN_VALUE, MAX_VALUE)):
                if flag == -1:
                    name += choice(CONSONANTS)
                else:
                    name += choice(VOWELS)
                    flag *= -1
            f.write(name.title() + '\n')

if __name__ == '__main__':
    gen_names(10, Path('names.txt'))



# Задание №3 Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# При достижении конца более короткого файла,
# возвращайтесь в его начало.

from pathlib import Path
from typing import TextIO

def read_or_begin(fd: TextIO) -> str:
    text = fd.readline()
    if text == '':
        fd.seek(0)
        text = fd.readline()
    return text.strip()


def sum_files(f1_name: Path, f2_name: Path, res_file: Path) -> None:
    with open(f1_name, 'r', encoding='UTF-8') as f1, \
        open(f2_name, 'r', encoding='UTF-8') as f2, \
        open(res_file, 'a', encoding='UTF-8') as f_res:
            len_f1 = sum(1 for _ in f1)
            len_f2 = sum(1 for _ in f2)
            for _ in range(max(len_f1, len_f2)):
                name = read_or_begin(f1)
                num_int, num_fl = read_or_begin(f2).split(' | ')
                mult = int(num_int)*float(num_fl)
                f_res.write(f'{name.lower()} {-mult}\n') if mult < 0 \
                else f_res.write(f'{name.upper()} {int(mult)}\n') if mult > 0 else 42


if __name__ == '__main__':
    sum_files(Path('names.txt'), Path('numbers.txt'), Path('results.txt'))


# Задание №4 Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# расширение
# минимальная длина случайно сгенерированного имени, по умолчанию 6
# максимальная длина случайно сгенерированного имени, по умолчанию 30
# минимальное число случайных байт, записанных в файл, по умолчанию 256
# максимальное число случайных байт, записанных в файл, по умолчанию 4096
# количество файлов, по умолчанию 42
# Имя файла и его размер должны быть в рамках переданного диапазона.

from random import choices, randint
from string import ascii_lowercase, digits


# def gen_files(ext: str, min_name: int = 6, max_name: int = 30, min_size: int = 256,
# max_size: int = 4096, file_count: int = 42) -> None:
#     for _ in range(file_count):
#         name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name, max_name)))
#         data = bytes(randint(0,255) for _ in range(randint(min_size,max_size)))
#         with open(f'{name}.{ext}', 'wb') as f:
#             f.write(data)
#
#
# if __name__ == '__main__':
#     gen_files("bin", file_count=3)

# Задание №5
# Доработаем предыдущую задачу.
# Создайте новую функцию которая генерирует файлы с разными расширениями.
# Расширения и количество файлов функция принимает в качестве параметров.
# Количество переданных расширений может быть любым.
# Количество файлов для каждого расширения различно.
# Внутри используйте вызов функции из прошлой задачи.

from random import choices, randint
from string import ascii_lowercase, digits


# def gen_files(ext: str, min_name: int = 6, max_name: int = 30, min_size: int = 256,
# max_size: int = 4096, file_count: int = 42) -> None:
#     for _ in range(file_count):
#         name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name, max_name)))
#         data = bytes(randint(0,255) for _ in range(randint(min_size,max_size)))
#         with open(f'{name}.{ext}', 'wb') as f:
#             f.write(data)

def num_files(**kwargs) -> None:
    for ext, num in kwargs.items():
        gen_files(ext, file_count=num)

if __name__ == '__main__':
# gen_files("bin", file_count=5)
    num_files(bin=2, jpeg =1)

# Задание №6
# Дорабатываем функции из предыдущих задач.
# Генерируйте файлы в указанную директорию — отдельный параметр функции.
# Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

from random import choices, randint, randbytes
from string import ascii_lowercase, digits
from pathlib import Path
import os


def gen_files(ext: str, min_name: int = 6, max_name: int = 30, min_size: int = 256,
              max_size: int = 4096, file_count: int = 42) -> None:
    for _ in range(file_count):
        while True:
            name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name, max_name)))
            if not Path(f'{name}.{ext}').is_file():
                break
            data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
            with open(f'{name}.{ext}', 'wb') as f:
                f.write(data)


def gen_different_files(directory: Path, **kwargs) -> None:
    if isinstance(directory, str):
        directory = Path(directory)
    if not directory.is_dir():
        directory.mkdir(parents=True)
        os.chdir(directory)
    for ext, numbers in kwargs.items():
        gen_files(ext, file_count=numbers)


if __name__ == '__main__':
    gen_different_files(r"C:\Users\User\PycharmProjects\pythonProject\test\spam", txt=2, doc=4, bin=3)

# Задание №7
# Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# Каждая группа включает файлы с несколькими расширениями.
# В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

from pathlib import Path
import os
import shutil
from random import choices, randint, randbytes
from string import ascii_lowercase, digits
from pathlib import Path
import os


def gen_files(ext: str, min_name: int = 6, max_name: int = 30, min_size: int = 256,
    max_size: int = 4096, file_count: int = 42) -> None:
    for _ in range(file_count):
        while True:
            name = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_name, max_name)))
            if not Path(f'{name}.{ext}').is_file():
                break
        data = bytes(randint(0, 255) for _ in range(randint(min_size, max_size)))
        with open(f'{name}.{ext}', 'wb') as f:
            f.write(data)

def sort_files(path: str | Path, groups: dict[str:list[str]] = None) -> None:
    if not groups:
        groups = {
        Path("video"): ['avi', 'mov', 'mk4', 'mkv'],
        Path("images"): ['bmp', 'jpeg', 'jpg', 'png']
        }
    os.chdir(path)
    reverse_groups = {}
    for target_dir, ext_list in groups.items():
        if not target_dir.is_dir():
            target_dir.mkdir()
        for ext in ext_list:
            reverse_groups[f'.{ext}'] = target_dir
    print(reverse_groups)
    for file in path.iterdir():
        if file.is_file() and file.suffix in reverse_groups:
            file.replace(reverse_groups[file.suffix] / file.name)

def gen_different_files(directory: str | Path, **kwargs) -> None:
    if isinstance(directory, str):
        directory = Path(directory)
    if not directory.is_dir():
        directory.mkdir(parents=True)
    os.chdir(directory)
    for ext, numbers in kwargs.items():
        gen_files(ext, file_count=numbers)

if __name__ == '__main__':
    gen_different_files(r"C:\Users\User\PycharmProjects\pythonProject\test", avi=2,
                        doc=4, bin=3, jpg=5, mkv=6, png=3)
    sort_files(Path(r"C:\Users\User\PycharmProjects\pythonProject\test"))