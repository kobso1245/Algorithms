def has_left__node(tree, curr_index):
    if 2 * curr_index + 1 <= len(tree) - 1 and tree[2 * curr_index + 1] != 0:
        return True
    else:
        return False


def has_right_node(tree, curr_index):
    if 2 * curr_index + 2 <= len(tree) - 1 and tree[2 * curr_index + 2] != 0:
        return True
    else:
        return False


def is_BST(tree, curr_index, is_left):
    if not has_left__node(
            tree,
            curr_index) and not has_right_node(
            tree,
            curr_index):
        return tree[curr_index]
    left_val, right_val = (0, 0)

    if has_left__node(tree, curr_index) and has_right_node(tree, curr_index):
        left_val = is_BST(tree, 2 * curr_index + 1, True)
        right_val = is_BST(tree, 2 * curr_index + 2, False)

    elif has_left__node(tree, curr_index):
        left_val = is_BST(tree, 2 * curr_index + 1, True)
    else:
        right_val = is_BST(tree, 2 * curr_index + 2, False)

    if left_val and right_val:
        if tree[curr_index] > left_val and tree[curr_index] < right_val:
            if is_left:
                return max(left_val, right_val, tree[curr_index])
            else:
                return min(left_val, right_val, tree[curr_index])
        else:
            if is_left:
                return 2 ** 64
            else:
                return - (2 ** 64)
    elif not right_val:
        if tree[curr_index] > left_val:
            if is_left:
                return max(left_val, tree[curr_index])
            else:
                return min(left_val, tree[curr_index])
        else:
            if is_left:
                return 2 ** 64
            else:
                return - (2 ** 64)
    elif not left_val:
        if tree[curr_index] < right_val:
            if is_left:
                return max(right_val, tree[curr_index])
            else:
                return min(right_val, tree[curr_index])
        else:
            if is_left:
                return 2 ** 64
            else:
                return - (2 ** 64)


def full_BST(tree):
    res = is_BST(tree, 0, False)
    if res == -(2 ** 64):
        return False
    else:
        return True


def main():
    inp = input()
    arr = input().split(' ')
    res = full_BST([int(x) for x in arr])
    if res:
        print('YES')
    else:
        print('NO')

main()
