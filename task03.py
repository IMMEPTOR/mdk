# 1. Квадраты
for i in range(10, 100):
    rev = int(str(i)[::-1])
    if ((i + rev)**0.5) % 1 == 0:
        print(f"Найдено: {i} + {rev} = {i+rev}")

# 2. Чередование (буква, цифра...)
import random, string
res = ""
for i in range(1, 11):
    if i % 2 != 0: res += random.choice(string.ascii_letters)
    else: res += random.choice("0123456789")
print("Строка:", res)

# 3. Поменять местами 1-й и минимальный
arr = [10, 5, 20, 2, 8]
m_idx = arr.index(min(arr))
arr[0], arr[m_idx] = arr[m_idx], arr[0]
print("Массив:", arr)