from heapq import heappush, heappop

GRAPH = [[(2,2), (3, 10), (1, 6)],
         [(0,6),(3,3), (2, 3), (6, 8)],
         [(0,2),(1,3)],
         [(0,10),(1,3),(5,1)],
         [(6,3),(7,6)],
         [(3,1),(6,2)],
         [(1,8),(4,3),(7,12), (5, 2)],
         [(6,12),(4,6)]]

def test():
    print("dadada")



def djikstra(start, end, graph):
    dist = []
    prev = []
    passed = set()
    for i in range(len(graph)):
        dist.append(2 ** 63 - 1)
        prev.append(0)

    heap = []
    all_nodes = set(range(len(graph)))
    for i in range(len(graph[start])):
        dist[graph[start][i][0]] = graph[start][i][1]
        prev[graph[start][i][0]] = start
        heappush(heap, (graph[start][i][1],start, graph[start][i][0]))


    passed.add(start)
    while all_nodes != passed:
        try:
            elem = heappop(heap)
        except:
            break
        start = elem[2]

        for i in range(len(graph[start])):
            if graph[start][i][0] not in passed:
                dist[graph[start][i][0]] = min(dist[graph[start][i][0]], dist[start] + graph[start][i][1])
                heappush(heap, (graph[start][i][1], start, graph[start][i][0]))

        passed.add(start)

    return dist
def test(start, end, graph):
   dist = djikstra(start, end, graph)
   print(dist)

print(test(0,7,GRAPH))
