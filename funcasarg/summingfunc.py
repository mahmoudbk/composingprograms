def summing(n,kfunc):
    total ,k =0,1
    while k<=n:
        total,k  = total + kfunc(k) ,k+1
    return total 

def sum_naturals(n):
    def kfunc(x):
        return x
    return summing(n,kfunc)

#print(sum_naturals(100))

def sum_cubes(n):
    def kfunc(x):
        return x*x*x
    return summing(n,kfunc)

print(sum_cubes(100))
    
