strs = ["flower","flow","flight"]
prefix = []

transform = list(zip(*strs))

for i in transform:
    if len(set(i)) == 1:
        prefix.append(i[0])
    else:
        break

prefixstr = ""
print(prefixstr.join(prefix))


# Treats a list of string as a 2d matrix example below (truncate all elements to same size as smallest string first)
# [ [a,a,a], [a,a,b], [a,a,c]
# Transform the matrix so that rows become columns and columns become rows
# [a,a,a]    [a,a,a]
# [a,a,b]--->[a,a,a]  
# [a,a,c]    [a,b,c]
# First row is the first letters of each word, second row becomes list of seconds latters of each word
# Then we can easily see if a letter is has same position in each word
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