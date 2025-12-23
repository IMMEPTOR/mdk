# 1. Таблица умножения
n = int(input("Введите число: "))
for i in range(1, 11):
    print(f"{n} * {i} = {n * i}")

# 2. Знаки и нули
s = input("Введите строку: ")
count_signs = 0
before_zero = 0
for i in range(len(s)):
    if s[i] in "+-":
        count_signs += 1
        if i + 1 < len(s) and s[i+1] == '0':
            before_zero += 1
print(f"Всего знаков: {count_signs}, перед нулем: {before_zero}")

# 3. Сортировка по знаку (без изменения порядка внутри групп)
arr = [10, -5, 3, -2, 0, 7]
pos = [x for x in arr if x >= 0]
neg = [x for x in arr if x < 0]
print("Результат:", pos + neg)