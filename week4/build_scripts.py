def graph_builder():
    vertexes_count = int(input())
    names = input().split(' ')
    to_build_node = input()

    proper_name = to_build_node.split(' ')
    for elem in proper_name:
        if elem != '':
            to_build_node = elem
            break

    graph_table = {names[i]: [] for i in range(vertexes_count)}

    for i in range(vertexes_count):
        curr_vertexes = input().split(' ')[1::]
        for j in range(len(curr_vertexes)):
            graph_table[names[i]].append(curr_vertexes[j])

    return graph_table, to_build_node


def topo_sort(
        graph_table,
        curr_node,
        poseten_e_moje_bi_a_moje_bi_ne,
        v_putq_e,
        result):

    poseten_e_moje_bi_a_moje_bi_ne[curr_node] = 1
    v_putq_e[curr_node] = 1

    for naslednik in graph_table[curr_node]:
        if poseten_e_moje_bi_a_moje_bi_ne[
                naslednik] == 0 and v_putq_e[naslednik] == 0:
            v_putq_e[naslednik] = 1
            poseten_e_moje_bi_a_moje_bi_ne[naslednik] = 1
            res = topo_sort(
                graph_table,
                naslednik,
                poseten_e_moje_bi_a_moje_bi_ne,
                v_putq_e,
                result)
            if not res:
                return False
        elif poseten_e_moje_bi_a_moje_bi_ne[naslednik] and v_putq_e[naslednik]:
            return False

    v_putq_e[curr_node] = 0
    result.append(curr_node)
    return True


def start():
    table, start_node = graph_builder()
    poseten_e_moje_bi_a_moje_bi_ne = {elem: 0 for elem in table.keys()}
    v_putq_e = {elem: 0 for elem in table.keys()}
    result = []
    res = topo_sort(
        table,
        start_node,
        poseten_e_moje_bi_a_moje_bi_ne,
        v_putq_e,
        result)
    try:
        if res:
            print(" ".join([x for x in result]))
        else:
            print("BUILD ERROR")
    except Exception:
        print('BUILD ERROR')
start()
