# ИЗУЧЕНИЕ ФУНКЦИИ.

import random                                           # Импортируем библиотеку randon

def request_len():                                      # Функция 
    return int(input('Введи длину пароля: ' ))

len_pass = request_len()                                # Задаем переменную.    

while len_pass < 8 or len_pass > 20:                    # Прописываем условие.
    print('Пароль должен содержать от 8 до 20 символов')
    len_pass = request_len()   

simple = ["a", "b", "c", "d", "e", "f"]                 # Создаем списки чисел, букв и знаков для пароля
medium = [1, 2, 3, 4, 5]
hard = ['!', '#', "$", "*"]

medium.extend(simple)                                   # medium + simple перемешать.
hard.extend(medium)                                     # hard + medium + simple перемешать.

level_pass = input('Укажите сложность пароля (легкая, средняя или сложная): ')      # Запрос данных в переменную.
count_pass = int(input("Укажите колличество паролей: "))


def gen_pass(level):                                    # Функция генерирования пароля.
    data = ""                                           # Создание str переменной, пустой.
    for i in range(len_pass):                           
        symbol = random.choice(level)                   # ?????????? symbol что и откуда? level откуда вылез?????
        data += str(symbol)
    return data


if level_pass == "легкая":                              # Условие сложности пароля.
    password = gen_pass(level=simple)

elif level_pass == "средняя":
    password = gen_pass(level=medium)

elif level_pass == "сложная":
    password = gen_pass(level=hard)





print("\nInformation")
print(f"Длина пароля:           {len_pass}")
print(f"Сложность пароля:       {level_pass}")
print(f'Колличество паролей:    {count_pass}')

print("\n")    
print(f"Ваш пароль: {password}")
