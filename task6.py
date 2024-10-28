# Напишите функцию, которая сокращает дробь вида M/N.
# Где M и N - наутральные числа.
# В качестве аргументов она принимает числитель и знаменатель,
# выводит числитель и знаменатель после сокращения
#
# Пример:
# Ввод:
# 25 15
# Вывод:
# 5 3
def kit(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return (a + b)


def help(m, n):
    if m > n:
        a = kit(m, n)
        c = m // a
        b = n // a
        return(c,b)
    else:
        a = kit(m, n)
        b = (n // a)
        c = (m // a)
        return (c, b)

m = int(input())
n = int(input())
print(help(m, n))
