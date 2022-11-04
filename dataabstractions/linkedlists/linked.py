"""
*lets represent our linked list as a list where the first element is the head 
and the rest is a linked list
*if the rest is empty then it contains the word empty 
*and if our initial linked list is empty then its the word empty 
is_link,link,first,rest
"""

#example 
#four = [1,[2,[3,[4,'empty']]]]

empty = "empty"
# s is a linked list if its empty or its rest is a linked list itself 
def is_link(s):
    return s==empty or is_link(s[1])

def link(first,rest):
    assert is_link(rest)
    return [first,rest]

def first(s):
    assert is_link(s)
    assert s!=empty
    return s[0]

def rest(s):
    assert is_link(s)
    assert s!=empty
    return s[1]

four = link(1,link(2,link(3,link(4,empty))))


"""
>>> four = link(1,link(2,link(3,link(4,empty))))
>>> first(four)
1
>>> rest(four)
[2,[3,[4,"empty"]]]
"""

#lets get the list length 
def len_link(s):
    L=0
    if s==empty:
        return L
   
    while s!=empty:
        L+=1
        s = rest(s)
    return L

"""
>>> len_link(four)
4
"""

def get_item(s,i):
    assert i<=len_link(s),'list index out of range'
    
    while i>0:
        i-=1
        s = rest(s)
        
    return first(s)

"""
>>> get_item(four,1)
2
"""
"""
make len_link and get_item recursive 
"""

def len_link_recursive(s):
    if s==empty:
        return 0
  
    return  1 + len_link_recursive(rest(s))

def get_item_recursive(s,i):
    if i==0:
        return first(s)
 
    return get_item_recursive(rest(s),i-1)


#using recursion in order to extend a linked list 
def extend_link(s,t):
    assert is_link(s) and is_link(t)

    if s==empty:
        return t
    return link(first(s),extend_link(rest(s),t))
"""
>>> extend_link(four,four)
[1, [2, [3, [4, [1, [2, [3, [4, 'empty']]]]]]]]
"""
#applying a certain function to all elements of the list
def apply_to_all_link(f,s):
    assert is_link(s)

    if s==empty:
        return s
    return link(f(first(s)), apply_to_all_link(f, rest(s)))
"""
>>> apply_to_all_link(lambda x: x*x, four)
[1, [4, [9, [16, 'empty']]]]
"""
def keep_if_link(f,s):
    """Return a list with elements of s for which f(e) is true."""
    assert is_link(s)
    if s==empty:
        return s
    else :
        kept = keep_if_link(f,rest(s))
        
        if (f(first(s))):
            return link(first(s),kept)
        else :
            return kept



"""
>>> keep_if_link(lambda x:x%2==0,four)
[2, [4, 'empty']]
"""
    
def join_link(s,separator):
    """Return a string of all elements in a s seperated by a separator"""
    assert is_link(s)
    if s==empty:
        return s
    return str(first(s))+separator+join_link(rest(s),separator)

print(join_link(four,','))