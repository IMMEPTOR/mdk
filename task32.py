# 1. Кол-во цифр
n = input("Введите число: ")
print("Цифр в числе:", len([c for c in n if c.isdigit()]))

# 2. Удаление пунктуации
import string
s = input("Введите строку: ")
# string.punctuation содержит все знаки типа !,.,? и т.д.
res = "".join(c for c in s if c not in string.punctuation)
print("Результат:", res)

# 3. Разность сумм индексов
arr = [10, 5, 20, 5, 30] # индексы 0,2,4 (10,20,30) и 1,3 (5,5)
even_sum = sum(arr[0::2])
odd_sum = sum(arr[1::2])
print("Разность:", even_sum - odd_sum)