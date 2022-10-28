

def newton_update(f,df):
    def update(x):
        return x-f(x)/df(x)
    return update


def improve(update,close,guess=1):
    while not(close(guess)):
        guess= update(guess)

    return guess

def approx_eq(x,y,tolerance=1e-15):
    return abs(x-y)<=tolerance

def find_zero(f,df):
    def near_zero(x):
        return approx_eq(f(x),0)

    return improve(newton_update(f,df),near_zero)

def square_root_newton(a):
    def f(x):
        return x*x-a
    def df(x):
        return 2*x
    
    return find_zero(f,df)

#print(square_root_newton(2))
#>>> 1.4142135623730951
#print(square_root_newton(64))
#>>> 8.0


""" generalizing the calculation of f(x)=  x^n -a and its derivative"""

def power(x,n):
    result,i = x,1

    while i <n:
        result = result*x
        i = i+1
    return result

def n_root_newton(a,n):
    def f(x):
        return power(a,n) -a
    def df(x):
        return n*power(a,n-1)

    return find_zero(f,df)
print(power(2,3))

