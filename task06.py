import random, string

# 1. Числа
print("Числа:")
for i in range(20, 51):
    if i % 3 == 0 and i % 5 != 0:
        print(i, end=" ")

# 2. Группы по 3 символа
s = "abcdefghi" 
groups = []
for i in range(0, len(s) - 2, 3):
    part = list(s[i:i+3]) # взяли 3 буквы
    part[1] = random.choice(string.ascii_letters) # заменили среднюю
    groups.append("".join(part))
groups.sort()
print("\nГруппы:", groups)

# 3. Swap Max/Min
arr = [10, 50, 2, 30, 15]
idx_min = arr.index(min(arr))
idx_max = arr.index(max(arr))
arr[idx_min], arr[idx_max] = arr[idx_max], arr[idx_min]
print("Массив:", arr)