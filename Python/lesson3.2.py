#Homework
#Program that every 30 seconds press "f16" key for to be "active"

# import time
# import pyautogui
# while (True):
#     pyautogui.press("f16")
#     time.sleep(30)

"""1. https://www.codewars.com/kata/55dc4520094bbaf50e0000cb

Wilson primes satisfy the following condition. Let P represent a prime number.
Then,
((P-1)! + 1) / (P * P)
should give a whole number.
Your task is to create a function that returns true if the given number is a Wilson prime."""

#If your read deascription including wikipedia articles, then you knew that only three Wislon primes found: 5, 13 and 563
def am_i_wilson(n):
    return n in (5, 13, 563)

"""2. Create a function that returns the CSV representation of a two-dimensional numeric array.
Example:
input:
   [[ 0, 1, 2, 3, 4 ],
    [ 10,11,12,13,14 ],
    [ 20,21,22,23,24 ],
    [ 30,31,32,33,34 ]] 
output:
     '0,1,2,3,4\n'
    +'10,11,12,13,14\n'
    +'20,21,22,23,24\n'
    +'30,31,32,33,34'
Array's length > 2.
More details here: https://en.wikipedia.org/wiki/Comma-separated_values
"""

def to_csv_text(array):
    s = ""
    for row in array:
        s += ",".join(str(n) for n in row) + "\n"
    return s[:-1]  #exclude \n in the end

#return '\n\.join(','.join(map(str, line)) for line in array)
    #map(fn, iterator) kind of functional programming in Python

"""3. Create a function with two arguments that will return an array of the first n multiples of x.
Assume both the given number and the number of times to count will be positive numbers greater than 0.
Return the results as an array or list ( depending on language ).
Examples
count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
count_by(2,5) #should return [2,4,6,8,10]"""
def count_by(x, n):
    list(range(x, x * n + 1, x))

"""4. https://www.codewars.com/kata/52223df9e8f98c7aa7000062
How can you tell an extrovert from an introvert at NSA? Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.
I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it? According to Wikipedia, ROT13 (http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate jokes on USENET.
Hint: For this task you're only supposed to substitue characters. Not spaces, punctuation, numbers etc.

Test examples:
"EBG13 rknzcyr." -->
"ROT13 example."
"This is my first ROT13 excercise!" -->
"Guvf vf zl svefg EBG13 rkprepvfr!""""

