ans = 0
neg_flag = False
x = int(input("Введите число: "))
if x < 0:
    neg_flag = True
while ans**2 <x:
    ans = ans + 1
if ans**2 == x:
    print("Квадратный корень из", x, "равен", ans)
else:
    print(x, "- не идеальный квадрат")
    if neg_flag:
        print("Просто проверял ... ты имел в виду", -x, "?")
