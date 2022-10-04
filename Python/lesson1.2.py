"""https://www.codewars.com/kata/62ca07aaedc75c88fb95ee2f/python
You are given three integer inputs: length, minimum, and maximum.
Return a string that:
Starts at minimum
Ascends one at a time until reaching the maximum, then
Decends one at a time until reaching the minimum
repeat until the string is the appropriate length

Examples:
 length: 5, minimum: 1, maximum: 3   ==>  "12321"
 length: 14, minimum: 0, maximum: 2  ==>  "01210121012101"
 length: 11, minimum: 5, maximum: 9  ==>  "56789876567"

Notes:
length will always be non-negative
negative numbers can appear for minimum and maximum values
hyphens/dashes ("-") for negative numbers do count towards the length
the resulting string must be truncated to the exact length provided
return an empty string if maximum < minimum or length == 0
minimum and maximum can equal one another and result in a single number repeated for the length of the string
"""

# ascend_descend=lambda l,m,M:''.join(map(str,l*[*range(m,M+1),*range(M-1,m,-1)]))[:l]

def ascend_descend(length, minimum, maximum):
    a = ''
    i = 0
    j = minimum
    asc = True
    if maximum < minimum or length == 0:
        return(a)
    elif minimum == maximum:
        a = str(minimum)*length
        return a[0:length]
    else:
        while i <= length:
            if (asc):
                a = a + str(j)
                j = j + 1
            if (not asc):
                a = a + str(j)
                j = j - 1
            if (j == minimum or j == maximum):
                asc = not asc
            i = i + len(str(j))
            if (i < 0):
                i = i - 1
        return a[0:length]

print(ascend_descend(5, 1, 3))
print(ascend_descend(14, 0, 2))
print(ascend_descend(11, 5, 9))
print(ascend_descend(0, 5, 9))
print(ascend_descend(10, -1, 9))
print(ascend_descend(4, -5, -8))
