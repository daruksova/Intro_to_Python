# Задача 1. Дано натуральное число N. Напишите метод, который вернёт список простых множителей числа N и количество этих множителей.
# 60 -> 2, 2, 3, 5

def Readint():
    N = int(input('Введите число N: '))
    return N

def Task1(N):
    list = []
    count = 0
    div = 2
    while N >= 2:
        if N % div == 0:
            list.append(div)
            count += 1
            N /= div
        else:
            div += 1
    return list, count

print(Task1(Readint()))


