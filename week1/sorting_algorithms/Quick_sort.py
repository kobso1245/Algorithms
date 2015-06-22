
import random 
def sort_helper(sequence, start, end):
    if end - start <= 1:
        k = sequence[start]
        sequence[start] = sequence[end]
        sequence[end] = k
        return
    pivot = random.randint(start, end)
    pivot_value = sequence[pivot]

    k = sequence[pivot]
    sequence[pivot] = sequence[end]
    sequence[end] = k

    curr_start = start
    curr_end = end - 1
    while curr_start < curr_end:
        while curr_start < pivot:
            if pivot_value < sequence[curr_start]:
                break
            curr_start += 1

        while curr_end > pivot:
            if pivot_value > sequence[curr_end]:
                break
            curr_end -= 1

        if (curr_start == pivot and curr_end != pivot):
            k = sequence[pivot]
            sequence[pivot] = sequence[curr_end]
            sequence[curr_end] = k
            pivot += 1

        if curr_start != pivot and curr_end == pivot:
            k = sequence[pivot]
            sequence[pivot] = sequence[curr_start]
            sequence[curr_start] = k
            pivot -= 1


    if (curr_start == pivot and curr_end == pivot) and (sequence[curr_end]) 

    k = sequence[pivot]
    sequence[pivot] = sequence[end]
    sequence[end] = k
    print(pivot)
    print(sequence)
    print()
    sort_helper(sequence, pivot + 1, end)
    sort_helper(sequence, start, pivot - 1)

    return

def sort(sequence):
    sort_helper(sequence,0, len(sequence) - 1)
    return sequence

print(sort([1,3,2,5,7,8,12,56,43,80,120,6]))

