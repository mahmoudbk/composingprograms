""" in this try we are going to make a good approximation of the square root of 2
which is for reference something around 1.41421356237
we will work our way and allow a 0.00001 tolerance and in order to do that we will use
the bisection method where we solve the equation x^2-2 = 0
"""

"""we already know that f(1)=-1,f(2)=2 we surely can make bette guesses or make a function
to do that instead but we will leave that for later ..

"""




def improve(sqfunc,g1=1,g2=2):
    
    interval = [g1,g2]
    guess = 0.5*(interval[0]+interval[1])
    while not(approxeq(guess)):
        
        guess = 0.5*(interval[0]+interval[1])
        interval  = updateinterval(interval[0],interval[1],guess,sq2func)
        
       
    
       

    return guess

def updateinterval(x1,x2,y,func):
    if (func(x1)*func(y))<0:
        return [x1,y]
        
    return [x2,y]

def sq2func(x):
    return (x*x)-2

def approxeq(g):
    tolerance = 0.00000000000001
    return abs(sq2func(g,2))<=tolerance

print(improve(sq2func))