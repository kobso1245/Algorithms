from heap_sort import remove_top, insert_elem
def k_min(array, k):
    size = 0
    max_heap = []    
    for elem in array:
        insert_elem(max_heap, elem)
        size += 1
        if size > k:
            max_heap = remove_top(max_heap)[1]
    return remove_top(max_heap)[0]


