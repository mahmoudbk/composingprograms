"""
Aggregation. A third common pattern in sequence processing is to aggregate all values 
in a sequence into a single value.
 The built-in functions sum, min, and max are all examples of aggregation functions.

By combining the patterns of evaluating an expression for each element
, selecting a subset of elements, and aggregating elements, we can solve problems
 using a sequence processing approach.
"""

def devisors(n):
    return [1] + [i for i in range(2,n) if n%i==0]
def check_perfect_number(x):
    return sum(devisors(x))==x

def perfect_numbers_in_range(n):
    return [x for x in range(2,n) if sum(devisors(x))==x]



"""
>>> perfect_numbers_in_range(1000)
[6, 28, 496]
"""

"""
what we are trying to here is calculate the permiter beased on the area and the height
so given the area and the height the width is just the devision of the given ones
we can assert both the width and height evenly devide the area to ensure that 
the side lengths are integers 

"""

def width(height,area):
    assert area%height==0
    return area//height

def perimeter(width,height):
    return (width+height)*2

def minimum_permiters(area):
    perimeters = [perimeter(width(h,area),h) for h in devisors(area)]
    return min(perimeters)

# Higher-Order Functions 

def maping(map_fn,s):
    return [map_fn(x) for x in s]

def filtering(filter_fn,s):
    return [x for x in s if filter_fn(x)]
def reducing(reduce_fn,s,initial):
    reduced = initial 
    for x in s:
        reduced = reduce_fn(reduced,x)
    return reduced
def mul(x,y):
    return x*y
"""
>>> reducing(mul,[2,4,8],1)
64
"""

