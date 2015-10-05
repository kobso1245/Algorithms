def bfs(graph, start):
    que = [(start, 0)]
    passed = set()

    while que != []:
        curr_node = que.pop(0)
        for i in range(len(graph[curr_node[0]])):
            if graph[curr_node[0]][i] not in passed:
                passed.add((graph[curr_node[0]][i], curr_node[1] + 1))
                que.append((graph[curr_node[0]][i], curr_node[1] + 1))
                graph[
                    curr_node[0]][i] = (
                    graph[
                        curr_node[0]][i],
                    curr_node[1] + 1)


def make_graph():
    inp = input().split(' ')
    nodes_cnt = int(inp[0])
    lines_cnt = int(inp[1])

    graph = [-1 for x in range(nodes_cnt + 1)]

    for i in range(lines_cnt):
        row = input().split(' ')
        if graph[int(row[0])] == -1:
            graph[int(row[0])] = [int(row[1])]
        else:
            graph[int(row[0])].append(int(row[1]))

        if graph[int(row[1])] == -1:
            graph[int(row[1])] = [int(row[0])]
        else:
            graph[int(row[1])].append(int(row[0]))

    inp = input().split(' ')
    distanses = bfs_new(graph, int(inp[1]))

    for i in range(1000):
        passed = set()
        curr_level = 0
        curr_node = int(inp[0])
        res = dfs(graph, passed, i, curr_node, curr_level, distanses)
        if not res:
            return i - 1


def dfs(graph, passed, headstart, curr_node, curr_level, distanses):
    passed.add(curr_node)
    if distanses[curr_node] == curr_level + headstart:
        return False
    for elem in graph[curr_node]:
        if elem not in passed:
            res = dfs(
                graph,
                passed,
                headstart,
                elem,
                curr_level + 1,
                distanses)

            if res:
                return False

    return True


def bfs_new(graph, start):
    que = [(start, 0)]
    passed = set()
    passed.add(start)

    distanses = [0 for x in range(len(graph) + 1)]

    while que != []:
        curr_node = que.pop(0)

        for elem in graph[curr_node[0]]:
            if elem not in passed:
                passed.add(elem)
                distanses[elem] = curr_node[1] + 1
                que.append((elem, curr_node[1] + 1))
    return distanses

print(make_graph())
