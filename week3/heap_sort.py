def swap(elem1, elem2):
    k = elem1
    elem1 = elem2
    elem2 = k
    return (elem1, elem2)


def insert_elem(heap, elem):
    new_elem_pos = len(heap)
    heap.append(elem)
    heapify(heap, new_elem_pos)


def create_heap1(array):
    resulted_array = []
    last_element_index = 0
    for elem in array:
        resulted_array.append(elem)
        heapify(resulted_array, last_element_index)
        last_element_index += 1

    return resulted_array


def create_heap(array):
    last_ind = len(array) - 1
    start_node = (last_ind - 1) // 2
    for curr_node in range(start_node, -1, -1):
        left_child = 2 * curr_node + 1
        right_child = 2 * curr_node + 2
        while left_child <= last_ind:
            if right_child <= last_ind:
                max_elem = max(array[left_child], array[right_child])
                if max_elem <= array[curr_node]:
                    break
                else:
                    if array[left_child] == max_elem:
                        array[left_child], array[curr_node] = swap(
                            array[left_child], array[curr_node])
                        curr_node = left_child
                        left_child = 2 * curr_node + 1
                        right_child = 2 * curr_node + 2

                    else:
                        array[right_child], array[curr_node] = swap(
                            array[right_child], array[curr_node])
                        curr_node = right_child
                        left_child = 2 * curr_node + 1
                        right_child = 2 * curr_node + 2
            else:
                if array[curr_node] >= array[left_child]:
                    break
                else:
                    array[curr_node], array[left_child] = swap(
                        array[curr_node], array[left_child])
                    curr_node = left_child
                    left_child = 2 * curr_node + 1
                    right_child = 2 * curr_node + 2

    return array


def heapify(resulted_array, last_element_index):
    parrent_node = (last_element_index - 1) // 2
    while parrent_node >= 0:
        if isinstance(resulted_array[parrent_node], tuple):
            if resulted_array[parrent_node][
                    0] < resulted_array[last_element_index][0]:
                resulted_array[parrent_node], resulted_array[last_element_index] = swap(
                    resulted_array[parrent_node], resulted_array[last_element_index])
                last_element_index = parrent_node
                parrent_node = (parrent_node - 1) // 2
            else:
                return
        else:
            if resulted_array[parrent_node] < resulted_array[
                    last_element_index]:
                resulted_array[parrent_node], resulted_array[last_element_index] = swap(
                    resulted_array[parrent_node], resulted_array[last_element_index])
                last_element_index = parrent_node
                parrent_node = (parrent_node - 1) // 2
            else:
                return

    return


def reverse_heapify(unheapified_max_heap):
    curr_node = 0
    left_node = 1
    right_node = 2
    last_node = len(unheapified_max_heap) - 1
    while right_node <= last_node:
        if isinstance(unheapified_max_heap[left_node], tuple):
            max_elem = max(
                unheapified_max_heap[left_node][0],
                unheapified_max_heap[right_node][0])
            if unheapified_max_heap[left_node][0] == max_elem:
                new_curr_node = left_node
            else:
                new_curr_node = right_node
        else:
            max_elem = max(
                unheapified_max_heap[left_node],
                unheapified_max_heap[right_node])
            if unheapified_max_heap[left_node] == max_elem:
                new_curr_node = left_node
            else:
                new_curr_node = right_node

        unheapified_max_heap[curr_node], unheapified_max_heap[new_curr_node] = swap(
            unheapified_max_heap[curr_node], unheapified_max_heap[new_curr_node])
        curr_node = new_curr_node
        left_node = 2 * curr_node + 1
        right_node = 2 * curr_node + 2

    if left_node <= last_node:
        if isinstance(unheapified_max_heap[curr_node], tuple):
            if unheapified_max_heap[curr_node][
                    0] < unheapified_max_heap[left_node][0]:
                unheapified_max_heap[curr_node], unheapified_max_heap[left_node] = swap(
                    unheapified_max_heap[curr_node], unheapified_max_heap[left_node])
        else:
            if unheapified_max_heap[
                    curr_node] < unheapified_max_heap[left_node]:
                unheapified_max_heap[curr_node], unheapified_max_heap[left_node] = swap(
                    unheapified_max_heap[curr_node], unheapified_max_heap[left_node])

    return


def push_down(array):
    curr_node = 0
    last_ind = len(array) - 1
    left_child = 2 * curr_node + 1
    right_child = 2 * curr_node + 2
    while left_child <= last_ind:
        if right_child <= last_ind:
            max_elem = max(array[left_child], array[right_child])
            if max_elem <= array[curr_node]:
                break
            else:
                if array[left_child] == max_elem:
                    array[left_child], array[curr_node] = swap(
                        array[left_child], array[curr_node])
                    curr_node = left_child
                    left_child = 2 * curr_node + 1
                    right_child = 2 * curr_node + 2

                else:
                    array[right_child], array[curr_node] = swap(
                        array[right_child], array[curr_node])
                    curr_node = right_child
                    left_child = 2 * curr_node + 1
                    right_child = 2 * curr_node + 2
        else:
            if array[curr_node] >= array[left_child]:
                break
            else:
                array[curr_node], array[left_child] = swap(
                    array[curr_node], array[left_child])
                curr_node = left_child
                left_child = 2 * curr_node + 1
                right_child = 2 * curr_node + 2

    return array


def remove_top(max_heap):
    if len(max_heap) == 0:
        return -1, -1
    else:
        last_pos = len(max_heap) - 1
        top_elem = max_heap[0]
        max_heap[0], max_heap[last_pos] = swap(
            max_heap[0], max_heap[last_pos])
        del max_heap[-1]
        push_down(max_heap)
    return top_elem, max_heap


def heap_sort(array):
    result = []
    max_heap = create_heap(array)
    elem, new_max_heap = remove_top(max_heap)
    max_heap = new_max_heap
    while max_heap != -1:
        if isinstance(elem, tuple):
            result.append(elem[0])
        else:
            result.append(elem)
        elem, new_max_heap = remove_top(max_heap)
        max_heap = new_max_heap
    return result[::-1]


def test():
    num = input()
    array = input().split(' ')
    array = [int(x) for x in array]
    sorted_arr = heap_sort(array)
    print(" ".join([str(x) for x in sorted_arr]))

test()
