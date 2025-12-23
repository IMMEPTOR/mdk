# 1. Нечетные делители
n = int(input("N: "))
for i in range(1, n + 1):
    if n % i == 0 and i % 2 != 0:
        print(i, end=" ")

# 2. Гласные
s = input("\nСтрока: ").lower()
vowels = "aeiouy"
count = sum(1 for char in s if char in vowels)
print("Гласных:", count)

# 3. Нули в конец
arr = [0, 1, 0, 3, 12, 0, 5]
non_zeros = [x for x in arr if x != 0]
zeros = [x for x in arr if x == 0]
print("Результат:", non_zeros + zeros)