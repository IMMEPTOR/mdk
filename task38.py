# 1. Без повторов
for i in range(1000, 10000):
    s = str(i)
    if len(set(s)) == 4: print(i, end=" ")

# 2. Кол-во цифр
s = input("\nСтрока: ")
print("Цифр:", sum(c.isdigit() for c in s))

# 3. Swap Max/Min
arr = [10, 2, 30, 1, 5]
mi, mx = arr.index(min(arr)), arr.index(max(arr))
arr[mi], arr[mx] = arr[mx], arr[mi]
print("Итог:", arr)