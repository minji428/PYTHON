import numpy as np

a = [12334567891, 20500, 1100007, 900001, 9028, 100, 15, 8, 0]
b = ['만', '천', '백', '십', ""]
def print_num(i, j):
    qq = []
    for i in a :
        c = i//100000
        d = i%100000
        e = str(c)
        f = 10000
        j = 0
        k = []
        for l in range(5):
            k.append(d%10)
            d //= 10
            f //= 10
        k = k[::-1]
        v = 10000

        for l in range(5) :
            v //= 10
            if i> v:
                e += str(k[l])
            if k[l] != 0 :
                e += b[l]
        g = ""
        check = False
        for z in e :
            if z != '0':
                g += z
        qq.append(g)
    return qq


    #print(f'{i:,}', ())



for i in a:
    print_num(i)
