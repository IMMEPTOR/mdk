# 1. Сумма кратных 3
n = int(input("N: "))
print("Сумма:", sum(i for i in range(1, n + 1) if i % 3 == 0))

# 2. Инверсия регистра
s = input("Строка: ")
print("Результат:", s.swapcase())

# 3. Произведение ненулевых
arr = [1, 0, 2, 3, 0, 4]
res = 1
for x in arr:
    if x != 0: res *= x
print("Произведение:", res)