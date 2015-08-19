from heapq import heappush, heappop
GRAPH = [[0,9,5200,3,2,5200,5200,5200],
         [5200,0,7,2,5200,5200,9,5200],
         [7,5200,0,5200,5200,7,7,5200],
         [5200,2,5200,0,5200,5200,5200,5200],
         [5200,5200,5200,5200,0,5200,5,5200],
         [5200,3,5200,5200,5200,0,5200,5200],
         [5200,5200,5200,5200,5200,5200,0,5200],
         [5200,5200,5200,5200,5200,5200,4,0]]




def djikstra(graph):
    length = len(graph)
    for k in range(length):
        for i in range(length):
            for j in range(length):
                if graph[i][j] > graph[i][k]+graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    return graph

def test(start, end, graph):
    graph = djikstra(graph)
    print(graph[start][end])

test(0,5, GRAPH)
    

