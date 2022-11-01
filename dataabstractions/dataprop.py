def pair(x,y):
    def get(index):
        if index==0:
            return x
        return y

    return get

def select(p,i):
    return p(i)


"""
>>> p=pair(5,6)
>>> select(p,0)
5
>>> select(p,1)
6
"""
