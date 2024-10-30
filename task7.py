# Напишите функцию is_valid_triangle(side1, side2, side3),
# которая принимает в качестве аргументов три натуральных числа,
# и возвращает значение True, если существует невырожденный треугольник
# со сторонами side1, side2, side3, или False в противном случае.
def is_valid_triangle(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        print(a,b,c)
        return True
    else:
        return False
a = int(input())
b =int(input())
c = int(input())
print(is_valid_triangle(a,b,c))