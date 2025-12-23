# 1. Нечетные в диапазоне
n = int(input("N: "))
m = int(input("M: "))
for i in range(n, m + 1):
    if i % 2 != 0: print(i, end=" ")

# 2. Слова на 'A'
s = input("\nПредложение: ").upper()
words = s.split()
count = sum(1 for w in words if w.startswith('A'))
print("Количество слов на A:", count)

# 3. Среднее без краев
arr = [1, 2, 3, 4, 10] # min=1, max=10
trimmed = sorted(arr)[1:-1] # убираем первый и последний
print("Среднее:", sum(trimmed)/len(trimmed))