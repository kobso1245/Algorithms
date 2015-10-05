def sort(sequence):
    elems_cnt = len(sequence)
    for i in range(elems_cnt):
        p = i
        while(p > 0 and sequence[p] < sequence[p - 1]):
            k = sequence[p]
            sequence[p] = sequence[p - 1]
            sequence[p - 1] = k
            p -= 1

    return sequence
