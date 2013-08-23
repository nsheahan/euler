#http://projecteuler.net/problem=2
#previous, current and next
fp = 1
fc = 2
fib = [1]

while fc < 4000000:
    fn = fp + fc
    fp = fc
    fc = fn
    fib.append(fp)

print(sum(filter(lambda x: x % 2 == 0, fib)))