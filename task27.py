# 1. Числа на 7
print("Числа:", [i for i in range(1, 101) if i % 10 == 7])

# 2. Замена или дописка
s = input("Строка: ")
if '!' in s:
    print(s.replace('!', '.'))
else:
    print(s + '.')

# 3. Размах (Max - Min)
arr = [10, 2, 30, 1, 5]
print("Разность:", max(arr) - min(arr))