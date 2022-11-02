def plusOne(digits):
    str1 = ''
    num1 = 0
    ans = []
    for i in digits:
        str1 = str1 + str(i)
    num1 = int(str1)
    num1 += 1
    for i in str(num1):
        ans.append(int(i))
    return ans

digits = [9,9,9]
print(plusOne(digits))