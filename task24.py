# 1. Фибоначчи
k = int(input("Сколько чисел? "))
a, b = 0, 1
for _ in range(k):
    print(a, end=" ")
    a, b = b, a + b

# 2. Скрытие цифр
s = input("\nСтрока: ")
res = "".join('*' if c.isdigit() else c for c in s)
print(res)

# 3. Проверка порядка
arr = [1, 3, 5, 10]
is_sorted = all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
print("По возрастанию?", is_sorted)