# ИЗУЧЕНИЕ ФУНКЦИЙ.

# def сложение(NUM1, NUM2):
#     сумма = NUM1+NUM2
#     return(сумма)

# ответ = сложение(NUM1=15, NUM2=16)

# ответ2 = сложение(NUM1=13, NUM2=200)

# print(ответ)
# print(ответ2)

def max_num(список):        # Создаем функци.^ которая принимает значение в переменну. список
    result = max(список)    # Из списка вы,ираем максимальное число и со[раняем в результат ]
    return result 

числа = [1, 2, 3, 4, 5, 213]

# ответ = max_num(список=числа)
# print(ответ)

def min_num(список):
    result = min(список)
    return result

# ответ2 = min_num(список=числа)
# print(ответ2)

print(  min_num(числа))
print(  min(числа))
