# Задача 1. Дано натуральное число N. Найдите значение выражения: N + NN + NNN
# N может быть любой длины.
# N = 132: 132 + 132132 + 132132132 = 132264396

def Readint():
    N = input('Введите число N: ')
    return N

def Task1(N):
    return int(N) + int(N + N) + int(N + N + N)

print(Task1(Readint()))
