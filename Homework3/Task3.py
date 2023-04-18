# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. Бот должен, как минимум, 
# отвечать на фразы «привет», «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.

data = open('dictionary.txt', encoding = 'utf-8')
answers = data.readlines()
data.close()

dictionary = {}
flag = True

for i in range(len(answers)):
    line = answers[i].split(':')
    dictionary[line[0]] = line[1]

print(dictionary)

while flag:
    user_input = input("Введите вашу фразу: ").lower()
    if user_input == 'выход':
        flag = False
    elif user_input in dictionary:
        print(dictionary[user_input])
    else:
        print("Извините, я не знаю, как на это ответить\n")
