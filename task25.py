# 1. Таблица квадратов
for i in range(1, 11):
    print(f"{i} | {i*i}")

# 2. Сумма цифр в строке
s = input("Строка: ")
print("Сумма:", sum(int(c) for c in s if c.isdigit()))

# 3. Перестановка половин
arr = [1, 2, 3, 4, 5, 6]
mid = len(arr) // 2
res = arr[mid:] + arr[:mid]
print("Итог:", res)