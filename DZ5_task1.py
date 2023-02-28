# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
#
# 2 2
# 4

def sum(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    return 1 + sum(a, b - 1)

a = int(input('Введите число: '))
b = int(input('Введите число: '))
print(sum(a, b))