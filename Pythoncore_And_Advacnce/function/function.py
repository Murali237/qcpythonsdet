# def wish(name):
#     print("hi",name, "gd mrng my orange")
#
# wish("murali")
from pycparser.ply.yacc import resultlimit


# return statement

# def add(x,y):
#     return x+y
#
# result=add(100,200)
# print("the sum is :",result)
# print("the sum is =", add(200,300))

# to write a program for factorial of a given number
# def fact(num):
#     result = 1
#
#     while num >= 1:
#         result = result * num
#         num = num - 1
#
#     return result  # This should be outside the while loop
#
#
# print(fact(5))
# for i in range(1,6):
#     print(" the fact of ",i,"is :",fact(i))


#  return multiple values from the function

def sum_sub(a,b):
    sum = a+b
    sub = a-b
    return sum,sub

print(sum_sub(2000,4292))


# types of arguments
"""
1. positional argument
2.keyword argument
3.default argument
4.variable length argument
"""

#  variable lenght argument
"""
we can pass any number of arguments to our function, such type of arguments are called variable length arguments

we declare with * symbol as follows 
def f1(*n):

we can call this function and pass any number of    argumnets including zero

internally all the values are represented as tuple

"""

def sum(*n):
    total = 0
    for i in n:
        total = total+i
    print("the sum is ",total)

sum()
sum(100,200,300,400,500)




