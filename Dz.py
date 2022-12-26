n = int(input("Введите возраст от 1 до 99: "))
s = str(n)
g = int(s[-1])
d = int(s[0])
if n >= 1 and n <= 99:
    if g == 1 and n != 11:
        print("Мне", n, "год")
    elif g >= 2 and g <= 4 and d != 1:
        print("Мне", n, "года")
    else:
        print("Мне", n, "лет")
else:
    print("Возраст указан неверно")