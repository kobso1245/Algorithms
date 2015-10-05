def sort(sequence, start, end):
    if start >= end:
        return
    length = len(sequence) - 1

    sort(sequence, start, start + length // 2)
    sort(sequence, start + length // 2 + 1, end)

    first_part_pointer = start
    second_part_pointer = start + length // 2 + 1

    tmp_arr = []

    while first_part_pointer <= length // 2 or second_part_pointer <= end:
        if sequence[first_part_pointer] < sequence[second_part_pointer]:
            tmp_arr.append(sequence[first_part_pointer])
            first_part_pointer += 1

        else:
            tmp_arr.append(sequence[second_part_pointer])
            second_part_pointer += 1

    if second_part_pointer != end:
        tmp_arr.extend(
            sequence[
                second_part_pointer:end -
                second_part_pointer +
                1])

    if first_part_pointer != length // 2:
        tmp_arr.extend(
            sequence[
                first_part_pointer:length //
                2 -
                first_part_pointer +
                1])

    sequence[start: end - start + 1] = tmp_arr


def sort_a(sequence):
    sort(sequence, 0, len(sequence) - 1)
    return sequence

print(sort_a([1, 3, 2, 5, 7, 8, 12, 56, 43, 80, 6]))
