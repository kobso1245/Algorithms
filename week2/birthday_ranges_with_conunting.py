def bir_ran(birthdays, ranges):
    all_birthdays = [0 for x in range(366)]
    curr_birt_count = 0
    for birthday in birthdays:
        all_birthdays[birthday] += 1

    for i in range(366):
        curr_birt_count += all_birthdays[i]
        all_birthdays[i]  = curr_birt_count

    result = []
    for curr_range in ranges:
        if curr_range[1] == 365 and curr_range[0] == 0:
            result.append(curr_birt_count)
        elif curr_range[1] == 365:
            result.append(curr_birt_count - all_birthdays[curr_range[0] - 1])
        elif curr_range[0] == 0:
            result.append(all_birthdays[curr_range[1] + 1])
        elif curr_range[0] > 0 and curr_range[1] < 365:
            result.append(all_birthdays[curr_range[1]] - all_birthdays[curr_range[0] - 1])
        else:
            result.append("Out of range!")

    return result

