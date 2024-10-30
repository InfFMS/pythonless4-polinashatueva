# Напишите процедуру, которая выводит на экран
# запись переданного ей числа в римской системе счисления.
# Числа находятся в диапазоне [1, 3999]
# I - 1, V - 5, X - 10, L - 50, C  - 100, D - 500, M - 1000
# Пример:
# 2013
# MMXIII
def fun(n):
    A={0:"",1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII",9:"IX"}
    B={10:"X",20:"XX",30:"XXX",40:"XL",50:"L",60:"LX",70:"LXX",80:"LXXX",90:"XC",0:""}
    C={100:"C",200:"CC",300:"CCC",400:"CD",500:"D",600:"DC",700:"DCC",800:"DCCC",900:"CM",0:""}
    D={1000:"M",2000:"MM",3000:"MMM",0:""}
    a=n%10
    b=n%100-a
    c=n%1000-b-a
    d=n%10000-c-b-a
    print(D.get(d),C.get(c),B.get(b),A.get(a),sep = "")


n = int(input())
fun(n)

