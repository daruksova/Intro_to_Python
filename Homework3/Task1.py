# Задача 1. Создайте список. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

def Readint():
    N = int(input('Введите число N: '))
    return N

def Fibonacci(N):
    numbers = [1, 1]
    for i in range(2, N):
        numbers.append(numbers[i - 1] + numbers[i - 2])
    return numbers

print(Fibonacci(Readint()))