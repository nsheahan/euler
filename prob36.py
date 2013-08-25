def cleanBin(num):

    #pythons builtin bin() function outputs a string
    #with a leading '0b'. This function cleans that.

    return bin(num)[2:]


def isPalindrome(num):
    strnum = str(num)
    if strnum == strnum[::-1]:
        return True
    else:
        return False

dpal = []
for i in range(1, 1000000):
    if isPalindrome(i) and isPalindrome(cleanBin(i)):
        dpal.append(i)

print(sum(dpal))