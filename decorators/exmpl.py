"""
python provides this special context of applying higher-order functions as part 
of executing a def statement called a decorator 
"""   
#common example 

def trace(fn):
    def wrapped(x):
        print(f"-> {fn} ({x})")
        return fn(x)
    return wrapped


@trace
def triple(x):
    return 3*x



"""
>>>triple(12)
-> <function triple at 0x7f3476ff0f90>(12)
"""
"""
the code above is equivilant to this 
>>>triple = trace(triple)
"""

#if negative number it returns the absolute value else returns whatever the function f returns 
#which is the square of the number in this particular case 

def absneg(f):
    def wrapped(x):
        if x>0:
            return f(x)
        return -x
    return wrapped

@absneg
def squarepos(x):
    return x*x


"""
>>>squarepos(5)
25
squarepos(-2)
2
"""
