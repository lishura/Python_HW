# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку


from module_task1 import date_is_true, date_is_true_terminal


if __name__ == '__main__':
    print(date_is_true('06.02.1982'))
    date_is_true_terminal()