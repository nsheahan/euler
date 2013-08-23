#http://projecteuler.net/problem=3
from math import sqrt


def factor(num):
    if num == 1:
        return [1]
    pfac = []
    for i in range(2, int((num ** .5) + 1)):
        while num % i == 0:
            pfac.append(i)
            num /= i
    if num > 1:
        pfac.append(num)

    return pfac


constant = 600851475143
print(max(factor(constant)))