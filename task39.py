# 1. Делители
n = int(input("N: "))
for i in range(1, n + 1):
    if n % i == 0: print(i, end=" ")

# 2. Только abc
s = input("\nСтрока: ")
print("Только abc?", set(s).issubset(set("abc")))

# 3. Суммы половин
arr = [1, 2, 3, 4, 5, 6]
n = len(arr) // 2
print("Разность:", sum(arr[:n]) - sum(arr[n:]))