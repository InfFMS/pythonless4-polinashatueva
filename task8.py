# Напишите рекурсивную функцию, которая
# раскладывает натуральное число на простые сомножители.
#
# Пример:
# Ввод:
# 378
# Вывод:
# 2*3*3*3*7

def kakayrekursia(a):
    b= 2
    c =""
    while n >1:
        while n %b==0:
            c+=str(b)+"*"
            a //=1
        b+=1
    return c[:-1]
a = int(input())
print(kakayrekursia(a))