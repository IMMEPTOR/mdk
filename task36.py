import random

# 1. Знаки и нули
s = input("Введите строку: ")
plus_minus = 0
before_zero = 0
for i in range(len(s)):
    if s[i] in "+-":
        plus_minus += 1
        if i + 1 < len(s) and s[i+1] == '0':
            before_zero += 1
print(f"Всего знаков: {plus_minus}, перед нулем: {before_zero}")

# 2. Замена четных символов
s_list = list(input("Введите строку для замены: "))
for i in range(1, len(s_list), 2): # i=1, 3, 5... (четные места)
    if s_list[i] not in "ab": s_list[i] = 'a'
    else: s_list[i] = 'c'
print("Итог:", "".join(s_list))

# 3. Массив: первый и минимальный
arr = [random.randint(10, 90) for _ in range(15)]
print("До:", arr)
m_idx = arr.index(min(arr))
arr[0], arr[m_idx] = arr[m_idx], arr[0]
print("После:", arr)