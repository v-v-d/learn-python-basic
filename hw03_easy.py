# Постарайтесь использовать то, что мы прошли на уроке при решении этого ДЗ,
# вспомните про zip(), map(), lambda, посмотрите где лучше с ними, а где они излишни!

# Задание - 1
# Создайте функцию, принимающую на вход Имя, возраст и город проживания человека
# Функция должна возвращать строку вида "Василий, 21 год(а), проживает в городе Москва"


def get_user_meta_to_string(name: str, age: int, city: str):
    return f"{name}, {age} год(а), проживает в городе {city}"

# Задание - 2
# Создайте функцию, принимающую на вход 3 числа, и возвращающую наибольшее из них


def get_max_number(number_1: int, number_2: int, number_3: int) -> int:
    return max(number_1, number_2, number_3)

# Задание - 3
# Создайте функцию, принимающую неограниченное количество строковых аргументов,
# верните самую длинную строку из полученных аргументов


def get_longest_string(*args: str) -> str:
    return max(args, key=len)
