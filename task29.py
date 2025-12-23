# 1. Четные делители
n = int(input("N: "))
for i in range(1, n+1):
    if n % i == 0 and i % 2 == 0:
        print(i, end=" ")

# 2. Swap символов
s = list(input("\nСтрока: "))
if len(s) > 1:
    s[0], s[-1] = s[-1], s[0]
print("Результат:", "".join(s))

# 3. Последний индекс X
arr = [1, 2, 3, 2, 4, 5]
x = int(input("X: "))
# Идем с конца (reversed)
for i in range(len(arr)-1, -1, -1):
    if arr[i] == x:
        print("Последний индекс:", i)
        break