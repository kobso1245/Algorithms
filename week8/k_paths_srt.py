def topo_sort(incoming, outgoing):
    start_nodes = [elem for elem in incoming if len(elem) == 0]

