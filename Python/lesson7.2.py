"""1. https://www.codewars.com/kata/57bfea4cb19505912900012c

def symmetric_point(p, q):
    return [q[0] + (q[0] - p[0]), q[1] + (q[1] - p[1])]"""

"""2. https://www.codewars.com/kata/5a34b80155519e1a00000009/python
def multiple_of_index(arr):
    new_arr = []
    for i, el in enumerate(arr[1:], start = 1):
        if el % i ==0:
            new_arr.append(el)
    return(new_arr)"""

"""3. https://www.codewars.com/kata/57a77726bb9944d000000b06/python
def mango(quantity, price):
    return (quantity - quantity // 3) * price"""

"""4. https://www.codewars.com/kata/57ab2d6072292dbf7c000039/train/python
def correct_polish_letters(st):
    l = "ąćęłńóśźż"
    lt = "acelnoszz"
    for i in range(len(l)):
        st = st.replace(l[i],lt[i])
    return st

def correct_polish_letters(st):
    return st.translate(str.maketrans("ąćęłńóśźż", "acelnoszz"))"""

"""5. https://www.codewars.com/kata/542ebbdb494db239f8000046
def next_item(xs, item):
    it = iter(xs)
    for x in it:
        if x == item:
            break
    return next(it, None)"""

"""6.https://www.codewars.com/kata/517b2bcf8557c200b8000015
Fixing bugs"""