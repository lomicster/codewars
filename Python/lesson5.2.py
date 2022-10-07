"""Variables
https://www.codewars.com/kata/50ee6b0bdeab583673000025/python
a = "code"
b = "wa.rs"
name = a + b
https://www.codewars.com/kata/5859d3325a8a0747180000c6/train/python
def hello(name):
   return(f'Hello, {name}')
https://www.codewars.com/kata/55a70521798b14d4750000a4/train/python
def greet(name):
    return(f'Hello, {name} how are you doing today?')
"""

"""Type casting
https://www.codewars.com/kata/5265326f5fda8eb1160004c8
def number_to_string(num):
    return str(num)
https://www.codewars.com/kata/544675c6f971f7399a000e79
def string_to_number(s):
    return int(s)
https://www.codewars.com/kata/563d59dd8e47a5ed220000ba/train/python
def get_sum_of_digits(num):
    sum = 0
    digits = str(num)
    for x in digits:
        sum+=int(x)
    return sum
"""

"""strings
https://www.codewars.com/kata/57a0556c7cb1f31ab3000ad7/solutions/python
def make_upper_case(s):
    return s.upper()
https://www.codewars.com/kata/57f759bb664021a30300007d/train/python
def switcheroo(s):
    return s.replace("a", "A").replace("b","a").replace("A","b")
https://www.codewars.com/kata/5b180e9fedaa564a7000009a/solutions/python
def solve(s):
    count_up=0
    count_lo=0
    for i in s:
        if i == i.upper():
            count_up += 1
        else:
            count_lo += 1
    if count_up > count_lo:
        return s.upper()
    else:
        return s.lower()
https://www.codewars.com/kata/5168bb5dfe9a00b126000018/python
def solution(string):
    return string[::-1]
"""
"""booleans
https://www.codewars.com/kata/56606694ec01347ce800001b/python
def is_triangle(a, b, c):
    return (a + b > c) and (b + c > a) and (a + c > b)
https://www.codewars.com/kata/55afed09237df73343000042/train/python
def is_lucky(n):
    return n % 9 == 0   
"""
"""if//else
https://www.codewars.com/kata/57202aefe8d6c514300001fd/train/python
def sale_hotdogs(n):
    return n * (100 if n < 5 else 95 if n < 10 else 90)
#1#https://www.codewars.com/kata/5810085c533d69f4980001cf/train/python

https://www.codewars.com/kata/5ad0d8356165e63c140014d4/train/python
final_grade(exam, projects):
    return 100 if (exam > 90 or projects > 10) else 90 if (exam > 75 and projects >= 5) else 75 if (exam > 50 and projects >= 2) else 0
#2#https://www.codewars.com/kata/55225023e1be1ec8bc000390/python

#3#https://www.codewars.com/kata/5a6d3bd238f80014a2000187/train/python


for loops
#4#https://www.codewars.com/kata/5865918c6b569962950002a1/train/python
https://www.codewars.com/kata/56b1f01c247c01db92000076/train/python
def double_char(s):
    sd = ""
    for i in s:
        i = i * 2
        sd += i
    return sd
    
def double_char(s):
    return "".join([x * 2 for x in s]) 
       
"""
"""range
https://www.codewars.com/kata/598057c8d95a04f33f00004e/solutions/python
def function(start_num, end_num): 
    return list(range(start_num+1, end_num))
#5#https://www.codewars.com/kata/56f69d9f9400f508fb000ba7/train/python

lists
https://www.codewars.com/kata/57cc975ed542d3148f00015b/train/python
def check(seq, elem):
    return elem in seq
#6#https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python

https://www.codewars.com/kata/580435ab150cca22650001fb/python
def filter_lucky(lst):
    return [el for el in lst if "7" in str(el)]
"""
#Resolve 6 more tasks!
