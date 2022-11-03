def tree(root_label,branches=[]):
    for branch in branches:
        assert is_tree(branch),'branches must be tress'

    return [root_label]+list(branches)
"""
create label , branches, is_tree,is_leaf
"""
def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

#for a tree to be a tree it must be one + all of its branches must be trees 
def is_tree(tree):
    #checking for the parent tree itself
    if type(tree)!=list or len(tree)<1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False

    return True

def is_leaf(tree):
    return not branches(tree)


"""
counting the number of leaves contained in a tree 
"""
def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else :
        count_branches = [count_leaves(b) for b in branches(tree) if is_leaf(tree)]
        return sum(count_branches)
        
