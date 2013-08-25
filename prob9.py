#http://projecteuler.net/problem=9


def isInt(num):
    #I feel filthy writing this
    return ((num - int(num)) == 0)

done = 0
for a in range(1, 1000):
    if done == 1:
        break
    for b in range(1, 1000):
        tmp = a + b
        clim = 1000 - tmp
        c2 = (a ** 2) + (b ** 2)
        c = c2 ** .5
        if c > clim:
            break
        elif isInt(c) and (a + b + c) == 1000:
            print(a * b * c)
            done = 1
            break