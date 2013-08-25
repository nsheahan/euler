#http://projecteuler.net/problem=7


def isPrime(num):
    for i in range(2, int(num ** .5 + 1)):
        if num % i == 0:
            return False
    return True

pc = 1
curr = 2
while pc != 10001:
    curr += 1
    if isPrime(curr):
        pc += 1

print(curr)