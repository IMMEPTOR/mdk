# 1. Билет
t = input("Введите 6 цифр: ")
if sum(map(int, t[:3])) == sum(map(int, t[3:])):
    print("Счастливый")
else:
    print("Нет")

# 2. Замена и счет цифр
s = list(input("Строка: "))
digits = 0
for i in range(len(s)):
    if s[i].isdigit(): digits += 1
    if (i + 1) % 2 == 0: # четное место
        s[i] = 'c' if s[i] in 'ab' else 'a'
print("Итог:", "".join(s), "Цифр:", digits)

# 3. Max на четных местах
arr = [5, 10, 2, 30, 1] # четные места: 10, 30
print("Max:", max(arr[1::2]))