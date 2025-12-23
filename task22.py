# 1. Поиск Максимума
n = int(input("Сколько чисел? "))
nums = [float(input("Число: ")) for _ in range(n)]
print("Максимум:", max(nums))

# 2. Очистка строки
s = input("Строка: ")
res = "".join(c for c in s if c.isalnum()) # alnum = буквы + цифры
print("Результат:", res)

# 3. Поиск X
arr = [1, 2, 3, 2, 4, 2, 5]
x = int(input("Что искать? "))
print(f"Число {x} встречается {arr.count(x)} раз")