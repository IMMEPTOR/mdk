# 1. Делится на 3 и 5
n = int(input("N: "))
for i in range(1, n + 1):
    if i % 15 == 0: print(i, end=" ")

# 2. Строка
s = input("\nСтрока: ")
if len(s) > 10:
    print(s.replace(" ", ""))
else:
    print("#" + s)

# 3. Второй максимум
arr = [10, 45, 2, 30, 45, 12]
unique_sorted = sorted(list(set(arr)), reverse=True)
print("\nВторой максимум:", unique_sorted[1] if len(unique_sorted) > 1 else "Нет")