"""
A for statement may include multiple names in its header to 'unpack' each element 
sequence to its respective element for example 

"""

pairs = [[1,2],[2,2],[2,3],[4,4]]


def count_same_pairs(arr):
    same_count  = 0 

    for x,y in arr :
        if x==y:
            same_count += 1
    return same_count

print(count_same_pairs(pairs))
#>>> 2