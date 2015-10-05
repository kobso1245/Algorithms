def k_path(graph, start, end, length):
    queue = []
    queue.append((start, 0))
    obh = [start]
    road_cnt = 0

    while queue != []:
        curr_node = queue.pop(0)

        for elem in graph[curr_node[0]]:
            if elem not in obh:
                queue.append((elem, curr_node[1] + 1))
            if elem == end:
                if curr_node[1] + 1 == length:
