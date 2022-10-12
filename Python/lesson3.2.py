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


'''4. https://www.codewars.com/kata/52223df9e8f98c7aa7000062
How can you tell an extrovert from an introvert at NSA? Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.
I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it? According to Wikipedia, ROT13 (http://en.wikipedia.org/wiki/ROT13) is frequently used to obfuscate jokes on USENET.
Hint: For this task you're only supposed to substitue characters. Not spaces, punctuation, numbers etc.

Test examples:
"EBG13 rknzcyr." -->
"ROT13 example."
"This is my first ROT13 excercise!" -->
"Guvf vf zl svefg EBG13 rkprepvfr!"'''

# def rot13(message):
#   return message.encode('rot13')
def rot13(message):
    abc = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM'
    r = ''
    for c in message:
        if c in abc:
            r += abc[abc.index(c) + 13]
        else:
            r += c
    return r

"""HW1. https://www.codewars.com/kata/5da9973d06119a000e604cb6"""

def counting_valleys(s):
    valleys = 0
    counter = 0
    is_valley = False
    for i in s:
        if i == 'U':
            counter += 1
        elif i == 'D':
            counter -= 1
        if counter < 0 and not is_valley:
            #valleys +=1
            is_valley = True
        if counter == 0 and is_valley:
            valleys += 1
            is_valley = False
    return valleys


"""Variant 2
def counting_valleys(s):
    level, valleys = 0, 0
    for step in s:
        if step == 'U' and level == -1:
            valleys += 1
        level += {'U': 1, 'F': 0, 'D': -1}[step]
    return valleys"""

"""HW2. Написать функцию/метод user_friendly_size:
-принимает на вход число (в байтах)
-возвращает float (2 decimal precision) в user friendly size (Kb, Mb, Gb, Tb)
-using test up to you (pytest or print with fn)
-challenge: pass the file path to the fn and fn shoud return "human" size

Examples:
user_friendly_size(9999)=>9.76Kb
user_friendly_size(9999999)=>9.54Mb"""




user_input = int(input('Enter the value in bytes: '))

def user_friendly_size():
    if user_input <= 1048576:
        result = f'{round(user_input/1024, 2)} Kb'
    elif user_input < 1073741824:
        result = f'{round(user_input/1048576, 2)} Mb'
    elif user_input < 1099511627776:
        result = f'{round(user_input/1073741824, 2)} Gb'
    else:
        result = f'{round(user_input/1099511627776)} Tb'
    return result

print(user_friendly_size())

# def tests():
#     assert user_friendly_size() == f'9.54 MB', f'user_input = {user_friendly_size()}'

import os
file_name = 'lesson3.2.py'
file_size = os.stat(file_name).st_size
print(file_size)

"""
import os
def user_friendly_size(file_size) -> str:
    symbols = ('B', 'kB', 'MB', 'GB', 'TB')
    if isinstance(file_size, str):                      # Если аргумент - строка
        if file_size.isdigit():                         # Если протупили и отправили число строкой
            file_size = int(file_size)
        else:
            file_size = os.stat(file_size).st_size       # Получим размер файла в байтах
    sym_index = int(math.log(file_size, 2) // 10)
    return f'{file_size / 2 ** (sym_index * 10):.2f} {symbols[sym_index]}'
"""