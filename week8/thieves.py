def get_em(tples, max_w, elems_cnt):
    max_v = 0
    weights = [tples[x][0] for x in range(len(tples))]
    values = [tples[x][1] for x in range(len(tples))]

    table = [[0 for x in range(elems_cnt + 1)] for y in range(max_w + 1)]

    for row in range(1, elems_cnt+1):
        for col in range(1, max_w+1):
            if row - weights[col-1]>=0:
                table[row][col] = max(table[row - weights[col-1]][col - 1] + values[col-1],
                                      table[row][col-1])
            else:
                table[row][col] = table[row][col - 1]

    return table
tples = [(3,5), (7,100), (1,1), (1,1), (2,3)]

print(get_em(tples, 5, 5))
