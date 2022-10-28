def curried_pow(x):
    def h(y):
        return pow(x,y)
    return h

"""
>>>curried_pow(2)(3)
8
"""

def map_to_range(start,end,f):
    while start<end:
        print(f(start))
        start+=1 
    
"""
>>>map_to_range(0,10,curried_pow(2))
1
2
4 
.
.
.
512
"""