from random import randrange


def has_sons(tree, curr_node):
    length = len(tree)
    if (2*curr_node + 1) > (length - 1) and (2*curr_node + 2) > (length - 1):
        return False
    else:
        return True

def has_left_son(tree, curr_node):
    length = len(tree)
    if (2*curr_node + 1) > (length - 1) or tree[2*curr_node + 1] == 0:
        return False
    else:
        return True

def has_right_son(tree, curr_node):
    length = len(tree)
    if (2*curr_node + 2) > (length - 1)or tree[2*curr_node + 2] == 0:
        return False
    else:
        return True




def test_is_BST(tree, curr_node,  is_left):
    if has_sons(tree, curr_node):
        left_subtree = None
        right_subtree = None
        if has_left_son(tree, curr_node):
            subtree_val = test_is_BST(tree, 2*curr_node + 1, is_left = True)
            if not subtree_val:
                return False
            if tree[curr_node] > subtree_val:
                left_subtree = tree[curr_node]
            else:
                return False
        if has_right_son(tree, curr_node):
            subtree_val = test_is_BST(tree, 2*curr_node + 2, is_left = False)
            if not subtree_val:
                return False
            if tree[curr_node] < subtree_val:
                right_subtree = subtree_val
            else:
                return False


        if left_subtree and right_subtree:
            if is_left:
                return max([left_subtree, right_subtree, tree[curr_node]])
            else:
                return min([left_subtree, right_subtree, tree[curr_node]])
        elif left_subtree:
            if is_left:
                return max([left_subtree, tree[curr_node]])
            else:
                return min([left_subtree, tree[curr_node]])
        elif right_subtree:
            if is_left:
                return max([right_subtree, tree[curr_node]])
            else:
                return min([right_subtree, tree[curr_node]])



    else:
        return tree[curr_node]

def is_BST(tree):
    answer = test_is_BST(tree, 0, False)
    if answer:
        return 'YES'
    else:
        return 'NO'

def testing():
    unique = set()
    length = 0
    while length < 100000:
        unique.add(randrange(1, 2000000000))
        length = len(unique)
    tree = list(unique)
    print(is_BST(tree))

def start():
    inp = input()

    elems = input().split(' ')

    tree = [int(elem) for elem in elems]
    print(is_BST(tree))

def other():
    for i in range(10000):
        testing()

start()
