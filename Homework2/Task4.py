# Задача 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

def ReadInt():
    N = int(input('Ввидите число N: '))
    return N

def GenerateList(N):
    list = []
    for i in range(-N, N + 1):
        list.append(i)
    return list

list = GenerateList(ReadInt())
print(f'Исходный массив {list}')
print(f'Измененный массив {list[-2:] + list[:-2]}')
