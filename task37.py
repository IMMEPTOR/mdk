# 1. Билет
t = input("Номер билета (6 цифр): ")
if sum(map(int, t[:3])) == sum(map(int, t[3:])):
    print("Счастливый")
else: print("Нет")

# 2. Мин в диапазоне
a = [10, 20, 5, 30, 2, 40]
n = int(input("От (индекс): "))
k = int(input("До (индекс): "))
print("Минимум:", min(a[n : k+1]))