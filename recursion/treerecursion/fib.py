"""
a tree recursion is a function that calls itself more than once for instance the fib
fib = 1,1,2,3,5,8,13 ..etc
"""
def fib(n):
    if n==1:
        return 1
    if n==2:
        return 1
    else:
        return fib(n-2)+fib(n-1)

"""
>>> fib(6)
8
"""