"""a normal approache of summing the digits of a certain number would look something like this """
def sum_digits(n):
    sum = 0
    while(n!=0):
        res = n%10
        sum+=res
        n  = (n-res)//10
   
    return sum
"""
>>>sum_digits(27)
9
>>>sum_digits(120)
3
>>>sum_digits(123)
6
"""

#a recursive way of doing that :

def sum_rec(n):
    sum =0
    if n%10==n:
        
        return n
    else :
        sum = n%10
        n = (n-n%10)//10
        
        return sum+sum_rec(n)
        

"""
>>>sum_rec(27)
9
>>>sum_rec(120)
3
>>>sum_rec(123)
6
"""