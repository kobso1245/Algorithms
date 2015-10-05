def bin_search(values, left_elem_to_find, right_elem_to_find):

    left = 0
    right = len(values) - 1
    curr = left + (right - left) // 2

    while left < right:
        if values[curr] >= left_elem_to_find:
            right = curr

        else:
            left = curr + 1
        curr = left + (right - left) // 2

    res_left = left
    right = len(values) - 1
    while left < right:
        if values[curr] > right_elem_to_find:
            right = curr
        else:
            left = curr + 1
        curr = left + (right - left) // 2

    res_right = right

    return res_left, res_right


def birthdays_count(birthdays, ranges):
    sorted_birthdays = birthdays.sort()
    res = []

    for curr_range in ranges:
        res_left, res_right = bin_search(
            birthdays, curr_range[0], curr_range[1])
        res.append(res_right - res_left)

    return res
