# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.

import math

for denominator in range(2, 12):
    for numerator in range(1, denominator):
        if math.gcd(numerator, denominator) == 1:
            fraction = numerator / denominator
            print(f"{numerator}/{denominator} = {fraction}")