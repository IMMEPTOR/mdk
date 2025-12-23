# 1. Сумма четных 1-100
print("Сумма:", sum(i for i in range(2, 101, 2)))

# 2. Замена a <-> b
s = input("Введите строку: ")
res = ""
for char in s:
    if char == 'a': res += 'b'
    elif char == 'b': res += 'a'
    else: res += char
print("Итог:", res)

# 3. Больше среднего
arr = [10, 20, 30, 40, 50]
avg = sum(arr) / len(arr)
count = len([x for x in arr if x > avg])
print(f"Среднее: {avg}, Кол-во элементов больше среднего: {count}")