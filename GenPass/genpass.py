import random

def request_len():
    return int(input('Введи длину пароля: ' ))

    
len_pass = request_len()

while len_pass < 8 or len_pass > 20:
    print('Пароль должен содержать от 8 до 20 символов')
    len_pass = request_len()   

simple = ["a", "b", "c", "d", "e", "f"]
medium = [1, 2, 3, 4, 5]
medium.extend(simple)
# print(f"TEST Medium: {medium}")
hard = ['!', '#', "$", "*"]
hard.extend(medium)
# print(f"TEST hard{hard}")

level_pass = input('Укажите сложность пароля (легкая, средняя или сложная): ')
count_pass = int(input("Укажите колличество паролей: "))


def gen_pass(level):
    data = ""
    for i in range(len_pass):
        symbol = random.choice(level)
        data += str(symbol)
    return data


if level_pass == "легкая":
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
