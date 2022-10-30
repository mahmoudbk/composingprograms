"""lets make a factorial function in both ways (a loop and recursion ) then compare the performace """
import time
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
#now the loop version 

def factloop(n):
    result = 1
    for i in range(1,n+1):
        result = result*i
    return result

"""
>>>factloop(3)
6
>>>factloop(4)
24
>>>factloop(5)
120

"""

#now lets compare them 

def calctime(f,testcases):
    avg = 0
    for i in testcases:
        start = time.time()
        f(i)
        end = time.time()
        avg += (end-start)
    return avg/len(testcases)

test = [3,4,5,6,7,8,200,500]
recursiontime = calctime(factorial,test)
looptime = calctime(factloop,test)
"""
>>>recursiontime-looptime
3.314018249511719e-05
"""

