###For-While Loops. If-Else statements###
##1 https://www.codewars.com/kata/57a0556c7cb1f31ab3000ad7
# def make_upper_case(s):
#     return s.upper()

##2 https://www.codewars.com/kata/5601409514fc93442500010b
# def better_than_average(class_points, your_points):
#     sum = 0
#     for point in class_points:
#         sum += point
#     class_avg = sum / len(class_points)
#     return your_points > class_avg

##3 https://www.codewars.com/kata/5808e2006b65bff35500008f
# def position(alphabet):
#     return(f"Position of alphabet: {ord(alphabet)-96}")

##4 https://www.codewars.com/kata/5302d846be2a9189af0001e4
# def say_hello(name, city, state):
#     return (f'Hello, {" ".join(name)}! Welcome to {city}, {state}!')

##5 https://www.codewars.com/kata/55225023e1be1ec8bc000390
# def greet(name):
#     if name == "Johnny":
#         return "Hello, my love!"
#     else:
#         return "Hello, {name}!".format(name=name)

##6 https://www.codewars.com/kata/563b74ddd19a3ad462000054
# def stringy(size):
#     return ''.join(str(i % 2) for i in range(1, size+1))

##7. https://www.codewars.com/kata/56c22c5ae8b139416c00175d
# def job_matching(candidate, job):
#     return candidate['min_salary'] * 0.9 <= job['max_salary']

##8 https://www.codewars.com/kata/557b5e0bddf29d861400005d
# def converter(mpg):
#     return round(mpg/4.54609188*1.609344, 2)

##9 https://www.codewars.com/kata/56b29582461215098d00000f
# def pipe_fix(nums):
#     return [x for x in range(nums[0], nums[-1]+1)]

##10 https://www.codewars.com/kata/57356c55867b9b7a60000bd7
#Ver1
# def basic_op(operator, value1, value2):
#     return eval(f'{value1} {operator} {value2}')

#Ver2
#     if operator == '+':
#         return value1 + value2
#     elif operator == '-':
#         return value1 -value2
#     elif operator == '*':
#         return value1 * value2
#     elif operator == '/':
#         return value1 / value2

##11 https://www.codewars.com/kata/57280481e8118511f7000ffa
# def split_and_merge(string_, separator):
#     return " ".join(separator.join(list(word)) for word in string_.split())

##12 https://www.codewars.com/kata/57241e0f440cd279b5000829
# def sum_mul(n, m):
#     if n == 0 or m == 0:
#         return 'INVALID'
#     if n == m:
#         return n - m
#     if n < 0 or m < 0:
#         return 'INVALID'
#
#     my_list = [number for number in range(n, m) if number % n == 0]
#     return sum(my_list)
##13 https://www.codewars.com/kata/58261acb22be6e2ed800003a
# def get_volume_of_cuboid(length, width, height):
#     return length * width * height

##14 https://www.codewars.com/kata/58bf9bd943fadb2a980000a7
# def who_is_paying(name):
#     return [name] if len(name) <= 2 else [name, name[:2]]
##15 https://www.codewars.com/kata/53da6d8d112bd1a0dc00008b
# def reverse_list(l):
#     l.reverse()
#     return(l)

##16 https://www.codewars.com/kata/5875b200d520904a04000003
#Ver1
# def enough(cap, on, wait):
#     if cap - on >= wait:
#         return 0
#     else:
#         return wait - (cap-on)

#Ver2
# def enough(cap, on, wait):
#     return max(0, wait - (cap - on))
##17 https://www.codewars.com/kata/57eae65a4321032ce000002d
# def fake_bin(str):
#     # Use a list comprehension to generate the result string
#     return ''.join(['0' if int(char) < 5 else '1' for char in str])

#Ver2
# def fake_bin(str):
#     res_str = ""
#     for char in str:
#         if int(char) < 5:
#             res_str += '0'
#         else:
#             res_str += '1'
#     return res_str

##18 https://www.codewars.com/kata/57e76bc428d6fbc2d500036d
# def string_to_array(s):
#     return s.split(" ")
