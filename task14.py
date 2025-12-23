# 1. Делители
n = int(input("N: "))
for i in range(1, n + 1):
    if n % i == 0: print(i, end=" ")

# 2. Удаление x перед abc
s = input("\nСтрока: ")
print(s.replace("xabc", "abc"))

# 3. Max отрицательный
arr = [-10, 5, -2, -30, 15]
neg = [x for x in arr if x < 0]
print("\nMax neg:", max(neg) if neg else "Нет")