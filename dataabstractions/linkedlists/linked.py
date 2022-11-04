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

print(get_item(four,1))
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
