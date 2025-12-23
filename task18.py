# 1. Сумма до нуля
total = 0
while True:
    num = int(input("Введи число (0 для стопа): "))
    if num == 0: break
    total += num
print("Сумма:", total)

# 2. Самое длинное слово
s = input("Введите предложение: ")
words = s.split()
longest = max(words, key=len)
print("Самое длинное слово:", longest)

# 3. Квадрат отрицательных
arr = [-2, 5, -3, 10, -1]
res = [x**2 if x < 0 else x for x in arr]
print("Итог:", res)