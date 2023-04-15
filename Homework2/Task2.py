# Задача 2. Выведите таблицу истинности для выражения ¬(X ∧ Y) ∨ Z.

def TruthTable():
    print("| X | Y | Z | ¬(X ∧ Y) ∨ Z |")
    print("|---|---|---|--------------|")
    for x in range(2):
        for y in range(2):
            for z in range(2):
                result = int(not(x and y) or z)
                print(f"| {x} | {y} | {z} |       {result}      |")


print(TruthTable())