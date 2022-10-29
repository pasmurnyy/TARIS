x = float(input("Введите число для x: "))
y = float(input("Введите число для y: "))
if x == y:
    print("x & y равны")
    if y != 0:
        print("следовательно, x/y равно", x/y)
elif x<y:
    print("x меньше")
elif x>y:
    print("y меньшеш")
print("Спасибо")