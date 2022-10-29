def compose1(f,g):
    return lambda x:f(g(x))

#we can even go further in making the arguments as lambdas functions 
func = compose1(lambda x:x*x,lambda y:y+1)


"""
>>>func(2)
8
"""