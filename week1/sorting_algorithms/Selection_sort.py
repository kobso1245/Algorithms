def sort(sequence):
    elems_count = len(sequence)
    for i in range(elems_count):
        min_elem = sequence[i]
        min_elem_pos = i
        for j in range(i, elems_count):
            if sequence[j] < min_elem:
                min_elem = sequence[j]
                min_elem_pos = j
        if min_elem_pos != i:
            k = sequence[min_elem_pos]
            sequence[min_elem_pos] = sequence[i]
            sequence[i] = k

    return sequence
