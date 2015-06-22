from heap_sort import insert_elem, remove_top

def k_lists(*args):
    lists = [x for x in args]
    for i in range(len(lists)):
        lists[i] = [(x, i, 0) for x in lists[i][::-1]]

    max_heap = []
    len_heap = 0
    result = []
    for lst in lists:
        len_heap += 1
        insert_elem(max_heap,lst[0])
    
    while len_heap > 0:
        max_elem, max_heap = remove_top(max_heap)
        len_heap -= 1
        value = max_elem[0]
        lst_num = max_elem[1]
        pos_in_lst = max_elem[2]
        result.append(value)
        if len(lists[lst_num]) - 1 > pos_in_lst:
            insert_elem(max_heap, (lists[lst_num][pos_in_lst+1][0], lists[lst_num][pos_in_lst+1][1], pos_in_lst+1))
            len_heap += 1

    return result[::-1]

print(k_lists([1,2,3,4], [5,6,7,8], [10,12,14]))
