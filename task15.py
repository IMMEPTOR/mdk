# 1. Сумма ряда
n = int(input("n: "))
print("Сумма:", sum(1/i for i in range(1, n+1)))

# 2. Строка 3 раза
s = input("Строка: ")
print(f"{s}, {s}, {s}")
print("Длина:", len(s))

# 3. Сумма max + min
arr = [10, 20, 5, 30, 15]
print("Сумма min и max:", min(arr) + max(arr))