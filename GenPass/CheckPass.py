# Писал с Салаватом.

# Напишите функцию check_password, которая проверяет переданный ей пароль на сложность и печатает на экран результат проверки.
# Сложным паролем будет считаться комбинация символов, в которой :
# Есть хотя бы 3 цифры.
# Есть хотя бы одна заглавная буква.
# Есть хотя бы один символ из следующего набора "!@#$%*"
# Общая длина не менее 10 символов.
# Если пароль прошел все проверки, функция должна вывести на экран фразу "Perfect password", в противном случае - "Easy peasy".


def check_password(пароль):
    numbers = check_numbers(data=пароль)
    upper = check_upper(data=пароль)
    symbol = check_symbol(data=пароль)
    count = check_count(data=пароль)

    # print(f"Numbers:   {numbers}")
    # print(f"Upper:     {upper}")
    # print(f"Symbol:    {symbol}")
    # print(f"lenght:    {count}")

    if (numbers and upper and symbol and count) is True:
        print("Perfect password")
    else:
        print("Easy peasy")

def check_numbers(data):
    list_number = []
    for element in data:
        if element.isdigit():
            list_number.append(element)
    if len(list_number) >= 3:
        return True
    else:
        return False

def check_upper(data):
    list_upper = []
    for символ in data:
        if символ.isupper():
            list_upper.append(символ)
    if len(list_upper) >= 1:
        return True
    else:
        return False

def check_symbol(data):
    znaki = "!@#$%*"
    list_znaki = []
    for symbol in data:
        if symbol in znaki:
            list_znaki.append(symbol)
    if len(list_znaki) >= 1:
        return True
    else:
        return False

def check_count(data):
    summa = len(data)
    if summa >= 10:
        return True
    else:
        return False


check_password(пароль="password1223QA!Z")