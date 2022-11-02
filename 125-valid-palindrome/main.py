def isPalindrome(s):
    s = s.lower()
    s = [x for x in s if x.isalpha() or x.isnumeric()]
    print(s)
    if s  == s[::-1]:
        return True
    else:
        return False

s = "0P"
print(isPalindrome(s))