"""
a tree has a root label and a squence branches every tree branch is a subtree and 
a tree with no branches is called a leaf, the root of every sub-tree is referred to
as a node so it would look something like this 
"""
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


#a tree with label 3 and two branches
tree1 = tree(3,[tree(1),tree(2,[tree(1),tree(1)])])
def print_this(arr):
    for ele in arr:
        print(ele)

print_this([tree1,label(tree1),branches(tree1),label(branches(tree1)[1]),is_leaf(branches(tree1)[0])])