def sort(sequence):
    helping_arr = []
    result_arr = []
    max_ele = max(sequence)
    for i in range(max_ele + 1):
        helping_arr.append(0)
    for elem in sequence:
        helping_arr[elem] += 1

    for i in range(max_ele + 1):
        while helping_arr[i]:
            result_arr.append(i)
            helping_arr[i] -= 1

    return result_arr

