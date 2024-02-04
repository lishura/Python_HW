# Задание №1 Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON.
# Имена пишите с большой буквы.
# Каждую пару сохраняйте с новой строки.

import json
# from pathlib import Path
#
#
# def convert_to_json(path: Path) -> None:
#     data = {}
#     with(
#     open(path, 'r', encoding='UTF-8') as f_read,
#     open(path.stem + '.json', 'w', encoding='UTF-8') as f_write
#     ):
#         for line in f_read:
#             name, number = line.split("|")
#             data[name.capitalize()] = float(number)
#             json.dump(data, f_write, indent=4, ensure_ascii=False)


# if __name__ == '__main__':
#     convert_to_json(Path('result.txt'))



# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и
# уровень доступа (от 1 до 7). После каждого ввода добавляйте новую информацию в JSON файл.
# Пользователи группируются по уровню доступа. Идентификатор пользователя выступает ключом для имени.
# Убедитесь, что все индентификаторы уникальны, независимо от уровня доступа. При перезапуске
# функции уже записанные в файл данные должны сохраняться.

# import json
# from pathlib import Path
#
#
# def input_user(path: Path) -> None:
#     unique_id = set()
#     if not path.is_file():
#         data = {str(level): {} for level in range(1, 8)}
#     else:
#         with open(path, 'r', encoding='UTF-8') as f_read:
#             data = json.load(f_read)
#             # unique_id = {id for id_name in data.values() for id in id_name.keys()}
#             for id_name in data.values():
#                 unique_id.update(id_name.keys())
#
#     while name := input("Введите имя пользователя: "):
#         level = input("Введите уровень доступа от 1 до 7: ")
#         user_id = input("Введите id пользователя: ")
#         if user_id not in unique_id:
#             unique_id.add(user_id)
#             data[level].update({user_id: name})
#             with open(path, 'w', encoding="UTF-8") as f_write:
#                 json.dump(data, f_write, indent=4, ensure_ascii=False)
#         else:
#             print("Такой id пользователя уже существует")
#
#
# if __name__ == '__main__':
#     input_user(Path("users.json"))


# Задание №3 Напишите функцию, которая сохраняет созданный в прошлом задании файл в формате CSV.

# import json
# from pathlib import Path
# import csv
#
# def json_to_csv(path: Path) -> None:
#     with open(path, 'r', encoding='UTF-8') as f_read:
#         data = json.load(f_read)
#     result = []
#     for level, id_name in data.items():
#         for id, name in id_name.items():
#             result.append({'level': int(level), 'id': int(id), 'name': name})
#
#     with open(path.stem + '.csv', 'w', encoding='UTF-8', newline='') as f_write:
#         csv_write = csv.DictWriter(f_write, fieldnames=['level', 'id', 'name'], dialect='excel-tab')
#         csv_write.writeheader()
#         csv_write.writerows(result)
#
#
#
# if __name__ == '__main__':
#     json_to_csv(Path('users.json'))

# Задание 4. Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.


# import json
# from pathlib import Path
# import csv
#
#
# def csv_to_json(from_path: Path, to_path: Path) -> None:
#     result = []
#     with open(from_path, 'r', encoding='UTF-8', newline='') as f_read:
#         csv_read = csv.reader(f_read, dialect='excel-tab')
#         for i, row in enumerate(csv_read):
#             if i != 0:
#                 level, id, name = row
#                 data = {
#                 "level": int(level),
#                 "id": f'{int(id):010}',
#                 "name": name.title(),
#                 "hash": hash(f'{name.title()}{int(id):010} ')
#                 }
#                 result.append(data)
#     with open(to_path, 'w', encoding='UTF-8') as f_write:
#         json.dump(result, f_write, indent=4, ensure_ascii=False)
#
#
# if __name__ == '__main__':
#     csv_to_json(Path('users.csv'), Path('new_users.json'))


# Задание 5. Напишите функцию, которая ищет json файлы в указанной директории и сохраняет их
# содержимое в виде одноимённых pickle файлов.


# import json
# from pathlib import Path
# import pickle
#
# def json_to_pickle(path: Path) -> None:
#     for obj in path.iterdir():
#         if obj.is_file() and obj.suffix == '.json':
#             with(
#                 open(obj, 'r', encoding='UTF-8') as f_read,
#                 open(obj.stem + '.pickle', 'wb') as f_write
#             ):
#                 data = json.load(f_read)
#                 pickle.dump(data, f_write)
#
#
# if __name__ == '__main__':
#     json_to_pickle(Path(r'C:\Users\User\PycharmProjects\pythonProject'))


# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из задачи 4 этого семинара.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.


import csv
from pathlib import Path
import pickle

def pickle_2_csv(path: Path) -> None:
    with open(path, 'rb') as f_read:
        data = pickle.load(f_read)
    headers = list(data[0].keys())
    with open(path.stem + '.csv', 'w', encoding='UTF-8', newline='') as f_write:
        csv_write = csv.DictWriter(f_write, fieldnames=headers, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
        csv_write.writeheader()
        csv_write.writerows(data)


if __name__ == '__main__':
    pickle_2_csv(Path('new_users.pickle'))


# Задание 7. Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Распечатайте его как pickle строку.

from pathlib import Path
import pickle
import csv


def csv_to_pickles(path: Path) -> None:
    with open(path, 'r', encoding='UTF-8', newline='') as f_read:
        csv_read = csv.reader(f_read, dialect='excel')
        result = []
        for i, row in enumerate(csv_read):
            if i != 0:
                result.append(dict(zip(headers, row)))
            else:
                headers = row

    print(pickle.dumps(result))


if __name__ == '__main__':
    csv_to_pickles(Path('new_users.csv'))





