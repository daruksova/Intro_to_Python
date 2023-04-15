# Задача 3. Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2


def CharCounter():

    str1 = input('Введите первую строку: ')
    str2 = input('Введите вторую строку: ')
    charCount = []

    for i in range(len(str1)):
        count = 0
        charCount.append(count)
        for j in range(len(str2)):
            if str1[i] == str2[j]:
                charCount[i] += 1
        print (f'Символ {str1[i]} - встречается {charCount[i]} раз/а')


CharCounter()

