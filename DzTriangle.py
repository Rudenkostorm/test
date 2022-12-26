a = float(input('Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))
if a+b > c and a+c > b and b+c > a:
    print('Треугольник с данными сторонами a,b,c существует!')
else:
    print('Треугольника с данными сторонами a,b,c не существует!')
