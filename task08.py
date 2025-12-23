# 1. Квадраты
for i in range(10, 21):
    print(i**2, end=" ")

# 2. Только abc
s = input("\nСтрока: ")
only_abc = True
for char in s:
    if char not in "abc":
        only_abc = False
        break
print("Только abc:", only_abc)

# 3. Индекс первого четного
arr = [1, 7, 4, 3, 8]
idx = -1
for i in range(len(arr)):
    if arr[i] % 2 == 0:
        idx = i
        break
print("Индекс:", idx)