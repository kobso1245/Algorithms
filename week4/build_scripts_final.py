def topo_sort(graph, start_node, visited, res, path):
    visited.add(start_node)
    path.add(start_node)
    for elem in graph[start_node]:
        if elem in path:
            return False
        if elem not in visited:
            res2 = topo_sort(graph, elem, visited, res, path)

        if not res2:
            return False
    res.append(start_node)
    path.remove(start_node)
    return True


def main():
    inp = int(input())

    names = input().split(' ')
    names_to_ind = {}
    ind_to_name = []
    cnt = 0
    for name in names:
        names_to_ind[name] = cnt
        ind_to_name.append(name)
        cnt += 1

    start_node = names_to_ind[input()]
    graph = []
    for i in range(inp):
        row = input().split(' ')
        graph.append([names_to_ind[row[j]]
                      for j in range(1, int(row[0]) + 1)])

    res = []
    visited = set()
    path = set()
    result = topo_sort(graph, start_node, visited, res, path)
    if result:
        print(" ".join([ind_to_name[res[i]] for i in range(len(res))]))
    else:
        print('BUILD ERROR')

main()
