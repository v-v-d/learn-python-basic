# Создайте собственный класс-исключение, который должен проверять
# содержимое списка на наличие только чисел. Проверить работу исключения
# на реальном примере. Необходимо запрашивать у пользователя данные и
# заполнять список только числами. Класс-исключение должен контролировать
# типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются
# бесконечно, пока пользователь сам не остановит работу скрипта, введя,
# например, команду “stop”. При этом скрипт завершается, сформированный
# список с числами выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить
# только числа и строки. При вводе пользователем очередного элемента
# необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить
# пользователю ввести текст (не число) и отобразить соответствующее
# сообщение. При этом работа скрипта не должна завершаться.


class NotIntError(Exception):
    pass


def get_float(val):
    try:
        return float(val)
    except ValueError as error:
        raise NotIntError(f'value must be a num, got {type(val)}.')


def get_nums_from_user(quit_symbol='q'):
    numbers = list()

    while True:
        val = input(f'Enter number ("{quit_symbol}" for quit): ')
        if val == quit_symbol:
            break
        try:
            numbers.append(get_float(val))
        except NotIntError as error:
            print(error)

    return numbers


if __name__ == '__main__':
    print(get_nums_from_user())
