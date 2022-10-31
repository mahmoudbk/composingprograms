def is_even(n):
    if n==0:
        return True
    else :
        return is_odd(n-1)
def is_odd(n):
    if n==0:
        return False
    else :
        return is_even(n-1)

#we can make a one recursive function 

def is_even2(n):
    if n==0:
        return True
    else :
        if(n-1==0):
            return False
        else:
            return is_even2((n-1)-1)