"""HW1. https://www.codewars.com/kata/5da9973d06119a000e604cb6
You need count how many valleys you will pass.
Start is always from zero level.
Every time you go down below 0 level counts as an entry of a valley, and as you go up to 0 level from valley counts as an exit of a valley.
One passed valley is equal one entry and one exit of a valley.
s='FUFFDDFDUDFUFUF'
U=UP
F=FORWARD
D=DOWN
To represent string above

(level 1)  __
(level 0)_/  \         _(exit we are again on level 0)
(entry-1)     \_     _/
(level-2)       \/\_/
So here we passed one valley"""


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


