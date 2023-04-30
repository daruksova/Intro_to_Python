# Задача 2. Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число. 
# Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов, совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет

import random

def ReadInt(text):
    N = int(input(text))
    return N

def CreateArray(N):
    array = [random.randint(0, 9) for _ in range (0, N)] 
    return array

def Task2(array, number):
    count = 0
    for i in range (0, len(array) - 2):
        if number == int(str(array[i]) + str(array[i + 1]) + str(array[i + 2])):
            count += 1
    if count > 0:
        print('Yes')
    else:
        print('No')

array = CreateArray(ReadInt('Введите длину массива: '))
print(array)
number = ReadInt('Введите трехзначное число: ')
print(number)
Task2(array, number)