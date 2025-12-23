# 1. Замена на 15
nums = []
for i in range(10):
    val = float(input("Введи число: "))
    if val > 15: val = 15
    nums.append(val)
print("Итог:", nums)

# 2. abc -> www
s = input("Строка: ")
if s.startswith("abc"): print("www" + s[3:])
else: print(s + "zzz")

# 3. y = 0.5x
x_arr = [2, 10, 5, 8]
y_arr = [0.5 * x for x in x_arr]
print("Y массив:", y_arr)