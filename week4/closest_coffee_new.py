def get_connected(points, stores_array, starting_point):
    if stores_array[starting_point]:
        return 0

    que = []
    que.append((starting_point, 0))
    passed = [starting_point]

    while len(que):
        curr_node, curr_level = que.pop(0)
        if stores_array[curr_node]:
            return curr_level
        for i in range(len(points[curr_node])):
            if points[curr_node][i] and stores_array[i]:
                return curr_level + 1
            if points[curr_node][i] and i not in passed:
                passed.append(i)
                que.append((i, curr_level + 1))
        
        
def start():
    rows_num = int(input())
    graph = []
    for i in range(rows_num):
        row = input().split(' ')
        graph.append([int(x) for x in row])
    starting_point = int(input())
    stores_array = input().split(' ')
    stores_array = [int(x) for x in stores_array]
    res = get_connected(graph, stores_array, starting_point)
    if res is None:
        print(-1)
    else:
        print(res)

start()
