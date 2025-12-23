# 1. Нечетные цифры
n = input("Число: ")
res = sum(int(d) for d in n if d.isdigit() and int(d) % 2 != 0)
print("Сумма нечетных цифр:", res)

# 2. Переворот слов
s = input("Строка: ")
words = s.split()
res = [w[::-1] for w in words]
print("Результат:", " ".join(res))

# 3. Фильтр по диапазону
arr = [5, 15, 25, 60, 10]
res = sum(x for x in arr if 10 < x < 50)
print("Сумма (10 < x < 50):", res)