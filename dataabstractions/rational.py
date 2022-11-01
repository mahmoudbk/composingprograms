"""
assuming we have these functions already built in as follows :
rational(n, d) returns the rational number with numerator n and denominator d.
numer(x) returns the numerator of the rational number x.
denom(x) returns the denominator of the rational number x.
"""




def add_rationals(x,y):
    nx,dx = numer(x),denom(x)
    ny,dy = numer(y),denom(y)

    return rational((nx*dy+ny*dx),dx*dy)


def mul_rationals(x,y):
    
    return rational(numer(x)*numer(y),denom(x)*denom(y))

def print_rational(x):
    print(numer(x),'/',denom(x))

def rationals_are_equal(x,y):
    return numer(x)*denom(y)==numer(y)*denom(x)

#representing rational numbers 


def numer(x):
    return x[0]
def denom(x):
    return x[1]

"""
>>> half = rational(1,2)
>>> print_rational(half)
1/2
>>> third = rational(1, 3)
>>> print_rational(mul_rationals(half, third))
1 / 6
>>> print_rational(add_rationals(third, third))
6 / 9
"""
"""
As the example above shows, our rational number implementation does not reduce 
rational numbers to lowest terms. We can remedy this flaw by changing 
the implementation of rational. If we have a function for computing the greatest
 common denominator of two integers, we can use it to reduce the numerator and the 
 denominator to lowest terms before constructing the pair
. As with many useful tools, such a function already exists in the Python Library.
"""

from fractions import gcd


def rational(n,d):
    g = gcd(n,d)
    return (n//g,d//g)

#abstraction barriers 

#example 
def square_rational(x):
    return mul_rationals(x,x)

#referring directly to numerators and denominators would violate one abstraction barrier

def square_rational_violating_twice(x):
    return [x[0]*x[0],x[1]*x[1]]

#Abstraction barries make programs easier to maintain and to modify. the fewer 
#functions the better 