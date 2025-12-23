# 1. Факториал
n = int(input("N: "))
res = 1
for i in range(1, n + 1): res *= i
print("Результат:", res)

# 2. Замена
s = input("Строка: ")
print(s.replace("word", "letter"))

# 3. Общие элементы
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]
print("Общие:", list(set(a) & set(b)))