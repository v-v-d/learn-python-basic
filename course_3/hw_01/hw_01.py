# 1. Написать функцию, реализующую вывод таблицы умножения размерностью AｘB.
# Первый и второй множитель должны задаваться в виде аргументов функции.
# Значения каждой строки таблицы должны быть представлены списком, который
# формируется в цикле. После этого осуществляется вызов внешней lambda-функции,
# которая формирует на основе списка строку. Полученная строка выводится в
# главной функции. Элементы строки (элементы таблицы умножения) должны разделять
# ся табуляцией.

get_str_from_sequence = lambda seq, spaces=4: ''.join(
    (f'{i!r:{spaces}}' for i in seq)
)


def get_mult_table_gen(cols, rows):
    return (
        (row if col == 0 else col * row or col for col in range(cols + 1))
        for row in range(rows + 1)
    )


for row in get_mult_table_gen(10, 10):
    print(get_str_from_sequence(row))

# 2. Дополнить следующую функцию недостающим кодом:
# def print_directory_contents(sPath):
# """
# Функция принимает имя каталога и распечатывает его содержимое
# в виде «путь и имя файла», а также любые другие
# файлы во вложенных каталогах.
#
# Эта функция подобна os.walk. Использовать функцию os.walk
# нельзя. Данная задача показывает ваше умение работать с
# вложенными структурами.
# """
# заполните далее
import os


def print_directory_contents(sPath):
    for name in os.listdir(sPath):
        path = os.path.join(sPath, name)
        if os.path.isdir(path):
            print_directory_contents(path)
        else:
            print(path, name)


print_directory_contents(os.getcwd())

# 3. Разработать генератор случайных чисел. В функцию передавать начальное и
# конечное число генерации (нуль необходимо исключить). Заполнить этими данными
# список и словарь. Ключи словаря должны создаваться по шаблону:
# “elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.
from random import randint


def get_random_num_seq(low, high, num_qty):
    if low and high:
        list_result = [randint(low, high) for _ in range(num_qty)]
        dict_result = {f'elem_{num}': num for num in list_result}
        return list_result, dict_result


print(get_random_num_seq(1, 10, 12))

# 4. Написать программу «Банковский депозит». Она должна состоять из функции и
# ее вызова с аргументами. Клиент банка делает депозит на определенный срок. В
# зависимости от суммы и срока вклада определяется процентная ставка:
# 1000–10000 руб (6 месяцев — 5 % годовых, год — 6 % годовых, 2 года — 5 %
# годовых). 10000–100000 руб (6 месяцев — 6 % годовых, год — 7 % годовых,
# 2 года – 6.5 % годовых). 100000–1000000 руб (6 месяцев — 7 % годовых,
# год — 8 % годовых, 2 года — 7.5 % годовых). Необходимо написать функцию,
# в которую будут передаваться параметры: сумма вклада и срок вклада. Каждый
# из трех банковских продуктов должен быть представлен в виде словаря с ключами
# (begin_sum, end_sum, 6, 12, 24). Ключам соответствуют значения начала и конца
# диапазона суммы вклада и значения процентной ставки для каждого срока. В
# функции необходимо проверять принадлежность суммы вклада к одному из
# диапазонов и выполнять расчет по нужной процентной ставке. Функция возвращает
# сумму вклада на конец срока.

DEPOSIT_RESOLVER = {
    # (min_sum, max_sum) : {months: year_percent, ...}
    (1000, 10000): {6: 7, 12: 8, 24: 7.5},
    (10000, 100000): {6: 6, 12: 7, 24: 6.5},
    (100000, 1000000): {6: 7, 12: 8, 24: 7.5},
}

def deposit(summ, months):
    for (min_sum, max_sum), percent_resolver in DEPOSIT_RESOLVER.items():
        if min_sum <= summ < max_sum and months in percent_resolver.keys():
            return summ + summ * percent_resolver[months] * 0.01 * months / 12

print(deposit(10000, 24))


# 5. Усовершенствовать программу «Банковский депозит». Третьим аргументом в
# функцию должна передаваться фиксированная ежемесячная сумма пополнения
# вклада. Необходимо в главной функции реализовать вложенную функцию подсчета
# процентов для пополняемой суммы. Примем, что клиент вносит средства в
# последний день каждого месяца, кроме первого и последнего. Например, при
# сроке вклада в 6 месяцев пополнение происходит в течение 4 месяцев. Вложенная
# функция возвращает сумму дополнительно внесенных средств (с процентами), а
# главная функция — общую сумму по вкладу на конец периода.

get_monthly_sum = lambda summ, rate, months: summ + summ * months * rate * 0.01

def chargeable_deposit(summ, months, monthly_sum):
    for (min_sum, max_sum), percent_resolver in DEPOSIT_RESOLVER.items():
        if min_sum <= summ < max_sum and months in percent_resolver.keys():
            rate = percent_resolver[months]
            return summ + (
                summ * rate * 0.01 * months / 12 +
                get_monthly_sum(monthly_sum, rate, months - 2)
            )

print(chargeable_deposit(10000, 24, 100))