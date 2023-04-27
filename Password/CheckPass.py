# Писал с Салаватом.

# Напишите функцию check_password, которая проверяет переданный ей пароль на сложность и печатает на экран результат проверки.
# Сложным паролем будет считаться комбинация символов, в которой :
# Есть хотя бы 3 цифры.
# Есть хотя бы одна заглавная буква.
# Есть хотя бы один символ из следующего набора "!@#$%*"
# Общая длина не менее 10 символов.
# Если пароль прошел все проверки, функция должна вывести на экран фразу "Perfect password", в противном случае - "Easy peasy".


def check_password(пароль):                                     # Создаем функцию на которую будут ссылаться остальные функции.
    numbers = check_numbers(data=пароль)                        # Переменные ссылаются на остальные функции.
    upper = check_upper(data=пароль)
    symbol = check_symbol(data=пароль)
    count = check_count(data=пароль)

    # print(f"Numbers:   {numbers}")                            # Проверочная распечатка функций.
    # print(f"Upper:     {upper}")
    # print(f"Symbol:    {symbol}")
    # print(f"lenght:    {count}")

    if (numbers and upper and symbol and count) is True:        # Условие (функция должна вывести на экран фразу "Perfect password", в противном случае - "Easy peasy").
        print("Perfect password")
    else:
        print("Easy peasy")

def check_numbers(data):                                        # Создаем функцию на проверку присутствия цифр в пароле. Должно быть 3 в пароле.
    list_number = []
    for element in data:
        if element.isdigit():                                   # .isdigit() возвращает цифры из пароля.                  
            list_number.append(element)                         # Добавляем найденную цифру в "list_number = []"
    if len(list_number) >= 3:
        return True
    else:
        return False

def check_upper(data):                                          # Создаем функцию на проверку присутствия заглавных букв. Должен быть хотя бы 1 в пароле.
    list_upper = []
    for символ in data:
        if символ.isupper():                                    # .isupper() возвращает заглавные буквы из пароля.
            list_upper.append(символ)                           # Добавляем найденную заглавную букву в "list_upper = []"
    if len(list_upper) >= 1:
        return True
    else:
        return False

def check_symbol(data):                                          # Создаем функцию на проверку присутствия знаков "!@#$%*". Должен быть хотябы 1 в пароле.
    znaki = "!@#$%*"                                             # Создаем переменную со знаками "!@#$%*"
    list_znaki = []
    for symbol in data:
        if symbol in znaki:
            list_znaki.append(symbol)
    if len(list_znaki) >= 1:
        return True
    else:
        return False

def check_count(data):                                          # СОздаем функцию на проверку колличества символов в пароле. Не меньше 10ти должно быть.
    summa = len(data)
    if summa >= 10:
        return True
    else:
        return False


check_password(пароль="password1223QA!Z")                       # Вводим пароль на проверку.