def ispalindrome(num):
    strnum = str(num)
    if strnum == strnum[::-1]:
        return True
    else:
        return False

largest = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if ispalindrome(product) and product > largest:
            largest = product

print(largest)