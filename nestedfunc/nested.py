def function1(func):
    x = 1 
    return x+func()

def function2(a):
    def function3():
        return a
    
    return function1(function3)

print(function2(7))
#>>>8