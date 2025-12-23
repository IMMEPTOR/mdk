# 1. Сумма цифр
n = input("Введите число: ")
print("Сумма цифр:", sum(int(d) for d in n if d.isdigit()))

# 2. Палиндром
s = input("Введите строку: ").lower().replace(" ", "")
if s == s[::-1]: print("Палиндром")
else: print("Нет")

# 3. Сумма между min и max
arr = [10, 1, 5, 8, 2, 20, 3]
i_min, i_max = arr.index(min(arr)), arr.index(max(arr))
start, end = min(i_min, i_max), max(i_min, i_max)
print("Сумма между ними:", sum(arr[start+1 : end]))