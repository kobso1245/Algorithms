def longest_subs(elems):
    table = [(0, "") for x in range(len(elems))]
    max_elem = elems[0]
    curr_max_elem = 0
    max_length = 0
    max_pos = len(elems)
    for i in range(len(elems) - 1, -1, -1):
        curr_max_elem = 0
        curr_max_index = i
        for j in range(i + 1, len(elems)):
            if elems[i] < elems[j]:
                if curr_max_elem < table[j][0]:
                    curr_max_elem = table[j][0]
                    curr_max_index = j
        if curr_max_index == i:
            table[i] = (1, str(elems[i]))
        else:
            table[i] = (table[curr_max_index][0] + 1, str(elems[i]) + table[curr_max_index][1])
            if table[i][0] > max_length:
                max_pos = i
                max_length = table[i][0]
    print(table[max_pos][0])
    print(table[max_pos][1])

longest_subs([6,1,5,3,1,7,2,5,7,4])
