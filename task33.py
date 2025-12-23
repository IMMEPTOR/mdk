# 1. Делители-квадраты
n = int(input("N: "))
for i in range(1, n + 1):
    if n % i == 0:
        if (i**0.5) % 1 == 0:
            print(i, end=" ")

# 2. Короткое слово
s = input("\nВведите строку: ")
words = s.split()
print("Самое короткое:", min(words, key=len))

# 3. Сколько минимальных
arr = [2, 5, 2, 8, 2, 10]
print("Кол-во минимальных элементов:", arr.count(min(arr)))