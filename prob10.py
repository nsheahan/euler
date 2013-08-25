#http://projecteuler.net/problem=10


def isPrime(num):
    for i in range(2, int(num ** .5 + 1)):
        if num % i == 0:
            return False
    return True

psum = 0
for i in range(2, 2000000):
    if isPrime(i):
        psum += i

print(psum)