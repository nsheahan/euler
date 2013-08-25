#http://projecteuler.net/problem=6
a = 5050 ** 2
b = sum([(x * x) for x in range(1, 101)])
print(max(a,b) - min(a,b))