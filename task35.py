# 1. Произведение цифр
n = input("Число: ")
res = 1
for d in n:
    if d.isdigit(): res *= int(d)
print("Произведение:", res)

# 2. Края строки
s = input("Строка: ")
if len(s) > 0 and s[0] == s[-1]: print("Да")
else: print("Нет")

# 3. Четные на нечетных местах
arr = [10, 2, 5, 4, 3, 6] # места 1,3,5 (индексы 0,2,4)
# Примечание: "нечетное место" — это индекс 0, 2, 4 (первый, третий...)
count = 0
for i in range(0, len(arr), 2):
    if arr[i] % 2 == 0:
        count += 1
print("Результат:", count)