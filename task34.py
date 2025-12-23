# 1. Простые числа (делится только на 1 и на себя)
n = int(input("N: "))
for num in range(2, n + 1):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0: break
    else: print(num, end=" ")

# 2. Замена пробелов
s = input("\nСтрока: ")
print(s.replace(" ", "_"))

# 3. Массив (кратные 3 -> 0)
arr = [3, 5, 9, 10, 12, 15, 1, 2]
res = [0 if x % 3 == 0 else x for x in arr]
print("Итог:", res)