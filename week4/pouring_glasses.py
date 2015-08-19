def graph_builder():
    capacities = input().split(' ')
    capacities = [int(x) for x in capacities]
    water = input().split(' ')
    water = [int(x) for x in water]
    pred = {(water[0], water[1], water[2], 0): -1}

    goal = int(input())

    graph = {(water[0], water[1], water[2], 0): []}
    que = [(water[0], water[1], water[2], 0)]

    res = []

    while len(que) != 0:
        curr_node = que.pop(0)
        variants = []

        capac_to = - curr_node[1] + capacities[1]
        if curr_node[0] > capac_to:
            variants.append((curr_node[0] - capac_to,
                             curr_node[1] + capac_to,
                             curr_node[2],
                             curr_node[3] + 1,
                             "1 2"))
        else:
            variants.append((0,
                             curr_node[1] + curr_node[0],
                             curr_node[2],
                             curr_node[3] + 1,
                             "1 2"))

        capac_to = - curr_node[2] + capacities[2]
        if curr_node[0] > capac_to:
            variants.append((curr_node[0] - capac_to,
                             curr_node[1],
                             curr_node[2] + capac_to,
                             curr_node[3] + 1,
                             "1 3"))
        else:
            variants.append((0,
                             curr_node[1],
                             curr_node[2] + curr_node[0],
                             curr_node[3] + 1,
                             "1 3"))

        capac_to = - curr_node[2] + capacities[2]
        if curr_node[1] > capac_to:
            variants.append((curr_node[0],
                             curr_node[1] - capac_to,
                             curr_node[2] + capac_to,
                             curr_node[3] + 1,
                             "2 3"))
        else:
            variants.append((curr_node[0],
                             0,
                             curr_node[2] + curr_node[1],
                             curr_node[3] + 1,
                             "2 3"))

        capac_to = - curr_node[0] + capacities[0]
        if curr_node[1] > capac_to:
            variants.append((curr_node[0] + capac_to,
                             curr_node[1] - capac_to,
                             curr_node[2],
                             curr_node[3] + 1,
                             "2 1"))
        else:
            variants.append((curr_node[0] + curr_node[1],
                             0,
                             curr_node[2],
                             curr_node[3] + 1,
                             "2 1"))

        capac_to = - curr_node[0] + capacities[0]
        if curr_node[2] > capac_to:
            variants.append((curr_node[0] + capac_to,
                             curr_node[1],
                             curr_node[2] - capac_to,
                             curr_node[3] + 1,
                             "3 1"))
        else:
            variants.append((curr_node[0] + capac_to,
                             curr_node[1],
                             0,
                             curr_node[3] + 1,
                             "3 1"))

        capac_to = - curr_node[1] + capacities[1]
        if curr_node[2] > capac_to:
            variants.append((curr_node[0],
                             curr_node[1] + capac_to,
                             curr_node[2] - capac_to,
                             curr_node[3] + 1,
                             "3 2"))
        else:
            variants.append((curr_node[0],
                             curr_node[1] + curr_node[2],
                             0,
                             curr_node[3] + 1,
                             "3 2"))

        

        i=0
        while i<6:
            new_node_1 = variants[i]
            if new_node_1[0] == goal or new_node_1[1] == goal or new_node_1[2] == goal:

                while curr_node != -1:
                    res.append(new_node_1[4])
                    new_node_1 = curr_node
                    curr_node = pred[curr_node]

                return new_node_1[3], res[::-1]
            try:
                graph[curr_node].append(new_node_1)
                que.append(new_node_1)
            except Exception:
                graph[curr_node] = [new_node_1]
            try:
                p = graph[new_node_1]
            except Exception:
                pred[new_node_1] = curr_node
                graph[new_node_1] = []
            i += 1
      
    return "IMPOSSIBLE"

def start():
    res = graph_builder()
    try:
        cnt, path = res
        print(cnt)
        for elem in path:
            print(elem)
    except Exception:
        print( "IMPOSSIBLE")
start()
