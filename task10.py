# 1. Сумма ряда
n = int(input("n: "))
s = sum(1/i for i in range(1, n+1))
print(f"Сумма: {s:.3f}")

# 2. Строки
s1, s2 = input(), input()
diff = abs(len(s1) - len(s2))
longer = s1 if len(s1) > len(s2) else s2
for _ in range(diff): print(longer)

# 3. Поиск вхождений
a, b = [1, 2], [1, 1, 2, 3]
for x in a:
    print(f"Элемент {x} найден в B {b.count(x)} раз(а)")