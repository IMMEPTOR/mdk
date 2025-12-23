# 1. Таблица на 7
for i in range(1, 11):
    print(f"7 * {i} = {7 * i}")

# 2. Сумма цифр в строке
s = input("Введите строку: ")
res = sum(int(char) for char in s if char.isdigit())
print("Сумма цифр:", res)

# 3. Среднее четных
arr = [2, 5, 8, 10, 3, 4, 7, 12, 1, 6]
evens = [x for x in arr if x % 2 == 0]
if evens:
    print("Среднее четных:", sum(evens) / len(evens))