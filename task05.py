# 1. Факториал
n = int(input("N: "))
p = 1
for i in range(1, n+1): p *= i
print("Произведение:", p)

# 2. Обрезка/Дописка
s = input("Строка: ")
if len(s) > 10: print(s[:6])
else: print(s.ljust(12, 'o'))

# 3. Половины
arr = [1, 2, 3, 4, 5, 6]
mid = len(arr)//2
print("Разность:", sum(arr[:mid]) - sum(arr[mid:]))