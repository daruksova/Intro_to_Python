# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа, 
# описывающие случайную возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [2, 7] или [4, 6, 7] и т.д.

def find_increasing_sequence(lst):
    increasing_sequence = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] > increasing_sequence[-1]:
            increasing_sequence.append(lst[i])
    return increasing_sequence

random_numbers = [5, 2, 3, 8, 1, 9, 4, 7, 6]
result = find_increasing_sequence(random_numbers)
print(result)
