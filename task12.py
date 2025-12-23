# 1. Числа без повторов
for i in range(1000, 10000):
    s_num = str(i)
    if len(set(s_num)) == 4: # set убирает дубли
        print(i, end=" ")

# 2. Индексы последнего символа
s = input("\nСтрока: ")
last = s[-1]
for i in range(len(s)):
    if s[i] == last:
        print(i, end=" ")

# 3. Мин в диапазоне
arr = [10, 20, 5, 3, 15, 8]
n = int(input("\nN: "))
k = int(input("K: "))
print("Min:", min(arr[n:k+1]))