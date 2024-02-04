# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.


DIV_HEX = 16

original_num: int = int(input("Введите целое число "))
num = original_num
h = '0123456789abcdef'
result: str = ''
while num > 0:
    result = h[num % DIV_HEX] + result
    num //= DIV_HEX
check = str(hex(original_num))
if result == check[2:]:
    print(f'Число {original_num} в шестнадцатиричной системе {result}')
else:
    print('Что-то пошло не так')


# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions


import fractions

first_fraction = str(input('Введите дробь вида a/b '))
second_fraction = str(input('Введите еще одну дробь вида a/b '))
f_1 = fractions.Fraction(int(first_fraction[0]),int(first_fraction[2]))
f_2 = fractions.Fraction(int(second_fraction[0]),int(second_fraction[2]))
sum_fraction = f_1 + f_2
mult_fraction = f_1 * f_2
print(f'сумма дробей {first_fraction} и {second_fraction} равна {sum_fraction}')
print(f'произведение дробей {first_fraction} и {second_fraction} равно {mult_fraction}')


