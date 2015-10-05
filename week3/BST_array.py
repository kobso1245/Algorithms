def is_BST(length, array):
    for i in range(len(array)):
        if array[i] and (length - 1) >= ((2 * i) + 1):
            if array[2 * i + 1] != 0 and array[2 * i + 1] > array[i]:
                return False
        if array[i] and (length - 1) >= ((2 * i) + 2):
            if array[2 * i + 2] != 0 and array[2 * i + 2] < array[i]:
                return False

    return True

print(is_BST(15, [8, 5, 15, 1, 0, 10, 18, 0, 7, 0, 0, 0, 12, 16, 20]))
