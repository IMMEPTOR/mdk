# 1. Сумма квадратов
n = int(input("N: "))
print("Сумма квадратов:", sum(i**2 for i in range(1, n+1)))

# 2. Найти цифры
s = input("Строка: ")
digits = [c for c in s if c.isdigit()]
print("Цифры в строке:", "".join(digits))

# 3. Есть ли отрицательные
arr = [5, 10, -1, 3]
has_neg = any(x < 0 for x in arr)
print("Есть отрицательные?", "Да" if has_neg else "Нет")