def cascade(n):
    if n<10:
        print(n)
    else :
        print(n)
        cascade(n//10)
        print(n)

cascade(2013)
"""
>>> cascade(2013)
2013
201
20
2
20
201
2013
"""