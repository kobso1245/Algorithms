def dfs(graph, curr_node, path, is_dir):

    res = True
    for i in range(len(graph[curr_node])):
        if graph[curr_node][i] != 0:
            el = graph[curr_node][i]
            if (is_dir[i] == 1 and el == 2) or (is_dir[i] == 2 and el == 1):
                return False
            else:
                is_dir[i] == el
            if not path[i]:
                path[i] = 1
                res = dfs(graph, i, path, is_dir)
                if not res:
                    return False
            else:
                return False
    path[curr_node] = 0
    return True


def main():
    is_dir = []
    inp = int(input())
    graph = []
    path = []
    start_node = []
    for i in range(inp):
        row = input().split(' ')
        graph.append([int(x) for x in row])
        is_dir.append(0)
        if 1 in graph[i] or 2 in graph[i]:
            start_node.append(i)
        path.append(0)


    for node in start_node:
        for i in range(inp):
            is_dir[i] = 0
            path[i] = 0
        is_dir[node] = 1
        res = dfs(graph, node, path, is_dir)
        if not res:
            print('false')
            return
    print('true')
main()
