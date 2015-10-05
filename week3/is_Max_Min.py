def has_left_child(tree, curr_node):
    length = len(tree)
    if (2 * curr_node + 1) > (length - 1):
        return False
    else:
        return True


def has_right_child(tree, curr_node):
    length = len(tree)
    if (2 * curr_node + 2) > (length - 1):
        return False
    else:
        return True


def tester2(tree, curr_node, curr_level):
    if not has_left_child(
            tree,
            curr_node) and not has_right_child(
            tree,
            curr_node):
        return tree[curr_node]
    if has_left_child(tree, curr_node):
        if curr_level % 2 == 1:
            min_subtree_left = tester(tree, 2 * curr_node + 1, curr_level + 1)
        else:
            max_subtree_left = tester(tree, 2 * curr_node + 1, curr_level + 1)
    if has_right_child(tree, curr_node):
        if curr_level % 2 == 1:
            min_subtree_right = tester(
                tree, 2 * curr_node + 2, curr_level + 1)
        else:
            max_subtree_right = tester(
                tree, 2 * curr_node + 2, curr_level + 1)

    if curr_level % 2 == 1:
        if min_subtree_left and min_subtree_right:
            min_elem = min(min_subtree_left, min_subtree_right)
            if tree[curr_node] > min_elem:
                return False
            else:
                return max(
                    [min_subtree_left, min_subtree_right, tree[curr_node]])
        elif min_subtree_left:
            if tree[curr_node] > min_subtree_left:
                return False
            else:
                return max([min_subtree_left, tree[curr_node]])
        elif min_subtree_right:
            if tree[curr_node] > min_subtree_right:
                return False
            else:
                return min([min_subtree_left, tree[curr_node]])
    else:
        if min_subtree_left and min_subtree_right:
            max_elem = max(max_subtree_left, max_subtree_right)
            if tree[curr_node] < max_elem:
                return False
            else:
                return min(
                    [min_subtree_left, min_subtree_right, tree[curr_node]])
        elif min_subtree_left:
            if tree[curr_node] > min_subtree_left:
                return False
            else:
                return max([min_subtree_left, tree[curr_node]])
        elif min_subtree_right:
            if tree[curr_node] > min_subtree_right:
                return False
            else:
                pass


def tester(tree, curr_node, curr_level):
    if not has_left_child(
            tree,
            curr_node) and not has_right_child(
            tree,
            curr_node):
        return (tree[curr_node], tree[curr_node])
    has_left = has_left_child(tree, curr_node)
    has_right = has_right_child(tree, curr_node)
    left_subtree = 0
    right_subtree = 0
    if has_left:
        left_subtree = tester(tree, 2 * curr_node + 1, curr_level + 1)
        if not left_subtree:
            return False
    if has_right:
        right_subtree = tester(tree, 2 * curr_node + 2, curr_level + 1)
        if not right_subtree:
            return False

    if has_left and has_right:
        max_elem = max([left_subtree[0], right_subtree[0], tree[curr_node]])
        min_elem = min([left_subtree[1], right_subtree[1], tree[curr_node]])

        if curr_level % 2 == 1:
            if tree[curr_node] > min_elem:
                return False
            else:
                return (max_elem, min_elem)
        else:
            if tree[curr_node] < max_elem:
                return False
            else:
                return (max_elem, min_elem)
    if has_left:
        max_elem = max([left_subtree[0], tree[curr_node]])
        min_elem = min([left_subtree[1], tree[curr_node]])

        if curr_level % 2 == 1:
            if tree[curr_node] > min_elem:
                return False
            else:
                return (max_elem, min_elem)
        else:
            if tree[curr_node] < max_elem:
                return False
            else:
                return (max_elem, min_elem)
    if has_right:
        max_elem = max([right_subtree[0], tree[curr_node]])
        min_elem = min([right_subtree[1], tree[curr_node]])

        if curr_level % 2 == 1:
            if tree[curr_node] > min_elem:
                return False
            else:
                return (max_elem, min_elem)
        else:
            if tree[curr_node] < max_elem:
                return False
            else:
                return (max_elem, min_elem)


def is_max(tree):
    res = tester(tree, 0, 1)
    if not res:
        return 'NO'
    else:
        return 'YES'


def start():
    inp = input()
    arr = input().split(' ')
    tree = [int(x) for x in arr]
    print(is_max(tree))
start()
