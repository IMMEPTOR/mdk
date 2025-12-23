# 1. Считаем числа
n = int(input("Сколько чисел? "))
pos, neg, zero = 0, 0, 0
for i in range(n):
    num = float(input("Введи число: "))
    if num > 0: pos += 1
    elif num < 0: neg += 1
    else: zero += 1
print(f"Плюс: {pos}, Минус: {neg}, Нули: {zero}")

# 2. Поиск x и w
s = input("Введи строку: ")
x_idx = s.find('x')
w_idx = s.find('w')
if x_idx == -1 and w_idx == -1: print("Нет таких букв")
elif x_idx != -1 and (x_idx < w_idx or w_idx == -1): print("Раньше 'x'")
else: print("Раньше 'w'")

# 3. Массив
import random
arr = [random.randint(-10, 30) for _ in range(15)]
print("Массив:", arr)
pos_list = [x for x in arr if x > 0]
if pos_list: print("Среднее:", sum(pos_list)/len(pos_list))