# 1. Квадраты
for i in range(10, 21): print(i**2, end=" ")

# 2. Половины массива
a = [1, 2, 3, 4, 5, 6]
m = len(a) // 2
print("\nНовый массив:", a[m:] + a[:m])

# 3. Замена word
s = input("\nВведите текст: ")
print(s.replace("word", "letter"))