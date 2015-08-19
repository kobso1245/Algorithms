def graph_builder():
    lines = int(input())
    names = input()
    nodes = names.split(' ')

    names_to_numbers = {nodes[i]: i for i in range(len(nodes))}

    to_be_built = input()

    incoming_vertexes = [[] for i in range(lines)]
    outgoing_vertexes = [[] for i in range(lines)]

    for i in range(lines):
        names = input().split(' ')[1::]
        for name in names:
            curr_node = names_to_numbers[i]
            incoming_vertexes[i].append(curr_node)
            outgoing_vertexes[curr_node].append(i)

    return (incoming_vertexes, outgoing_vertexes, names_to_numbers)

def topo_sort(incoming_vertexes, outgoing_vertexes):
    result = []
    vertex_count = len(incoming_vertexes)
    removed_vertexes = set()
    all_vertexes = set(x for x in range(vertex_count))

    while removed_vertexes != all_vertexes:
        for vertex in incoming_vertexes:
            if not len(vertex):
                #removing the edge
                removed_vertexes.add(vertex)

