# Задача 1. Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def Readline():
    N = int(input('Введите число N: '))
    return N

def Factorial(N):
    f = 1
    for i in range(1, N + 1):
        f = f * i
    return f

def PrintFactorialList(N):
    print(f'Список факториалов чисел от 1 до {N}:')
    for i in range(1, N + 1):
        print(Factorial(i), end = ' ')

PrintFactorialList(Readline())