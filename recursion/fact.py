"""lets make a factorial function in both ways (a loop and recursion ) then compare the performace """

#starting with recursion
def factorial(n):
    if n==1 or n==0:
        return 1
    else:
        return n*factorial(n-1)


"""
>>>factorial(3)
6
>>>factorial(4)
24
>>>factorial(5)
120
"""
