def convert_to_int(lst):
    res = 0
    stepen = 1
    for i in range(16):
        res += lst[15 - i] * stepen
        stepen *= 2
    return res


def reader():
    goal = convert_to_int([0 if x=='off' else 1 for x in input().split(' ')])

    graph = []
    switches_value = [0 for x in range(16)]

    for i in range(16):
        switches_value[i] = convert_to_int([int(x) for x in input().split(' ')])

    path = []
    passed = set()
    passed.add(0)
    print(goal)
    res = graph_builder(passed, goal, 0, path, switches_value, -1, 0)
    print(path)

def graph_builder(passed, goal, curr_node, path, switches_value, father, level):
    if level == 70:
        return False
    if curr_node == goal:
        return True

    for i in range(16):
        curr_new_val = switches_value[i] ^ curr_node
        if curr_new_val not in passed:
            if curr_new_val == goal:
                return True
            passed.add(curr_new_val)
            res = graph_builder(passed, goal, curr_new_val, path, switches_value ,i, level + 1)
            if res == True:
                path.append(i)
                return True

    return False

reader()
