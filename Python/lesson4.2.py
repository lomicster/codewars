# 1. https://www.codewars.com/kata/5715eaedb436cf5606000381
# def positive_sum(arr):
#     return(sum(filter(lambda x:x>=0, arr)))

"""2. https://www.codewars.com/kata/5b73fe9fb3d9776fbf00009e/python
Math solutin: max- min
def sum_of_differences(arr):
    return max(arr) - min(arr) if arr else 0

def sum_of_differences_2(arr):
    if len(arr) <=1:
        return 0
    diff = []
    arr.sort(reverse=True)
    for i in range(len(arr)):
        if i + 1 < len(arr):
            t = abs(arr[i] - arr[i+1])
            diff.append(t)
    return sum(diff)"""

3. https://www.codewars.com/kata/57e1e61ba396b3727c000251
import re
def string_clean(s):
    return re.sub(r'\d', '', s)

"""Homework:

https://www.codewars.com/kata/56c5847f27be2c3db20009c3

Regular expressions:
https://towardsdatascience.com/regular-expressions-clearly-explained-with-examples-822d76b037b4
https://regex101.com/
https://regexr.com/

Add new item (collections are passed by reference)
https://www.codewars.com/kata/566dc05f855b36a031000048/python

Ascend, Descend, Repeat
https://www.codewars.com/kata/62ca07aaedc75c88fb95ee2f

Your solutions - push to your personal github accounts for review:
<Name>: <github link>"""
