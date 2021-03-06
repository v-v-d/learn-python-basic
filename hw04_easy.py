# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]

lst = [1, 2, 4, 0]
new_lst = [el ** 2 for el in lst]

print(new_lst)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits_1 = ["яблоко", "банан", "киви", "арбуз"]
fruits_2 = ["апельсин", "банан", "мандарин", "арбуз"]

fruits_3 = [fruit for fruit in fruits_1 if fruit in fruits_2]

print(fruits_3)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4

from random import randint

lst_1 = [randint(-10, 100) for _ in range(1, 20)]

lst_2 = [num for num in lst_1 if num > 0 and num % 3 == 0 and num % 4 != 0]

print(lst_1)
print(lst_2)
