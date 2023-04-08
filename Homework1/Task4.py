# Задача 4. Напишите программу, которая на вход принимает число (N), а на выходе показывает все чётные числа от 1 до N.
# 5 -> 2, 4
# 8 -> 2, 4, 6, 8

number = int(input('Введите число: '))
i = 1

if number > 1:
    while i <= number:
        if i % 2 == 0:
            print(i)
        i += 1
else:
    while i >= number:
        if i % 2 == 0:
            print(i)
        i -= 1

