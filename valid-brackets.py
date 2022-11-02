from pickle import FALSE
from readline import append_history_file


def isValid(s):
    if s[0] == ')' or s[0] == '}' or s[0] == '}' or len(s)%2 != 0:
        return False

    close = []


    for i in s:
        if i == '(':
            close.append(')')
        elif i == '{':
            close.append('}')
        elif i == '[':
            close.append(']')
        elif len(close)>0 and i == close[-1]:
            close.pop()
        else:
            return False

    if len(close) == 0:
        return True

s = "(){}}{"
print(isValid(s))


# First ensure it doesn't start with closing bracket or len isn't odd
# Create list 'close'. This tracks what brackets needs to be closed.
# If we see a '(' we need to close it. We append ')' to close.
# For each item in str, we either append something that needs to be closed in 'close', or if it closes a bracket (if its equal to last item in close).
# Closing can be done by popping final item in 'close'. Always popping ensures we are closing in correct order
# If append in incorrect order it returns false
# It returns true if it runs through entire list and without returning flase
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#