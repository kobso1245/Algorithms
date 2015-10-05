def longest(first, second):
    table = [[0 for x in range(len(second) + 1)]
             for y in range(len(first) + 1)]

    for row in range(1, len(first) + 1):
        for col in range(1, len(second) + 1):
            if first[row - 1] == second[col - 1]:
                table[row][col] = table[row - 1][col - 1] + 1
            else:
                table[row][col] = 0

    max_el = 0
    tple = None
    for i in range(1, len(first) + 1):
        for j in range(1, len(second) + 1):
            if table[i][j] > max_el:
                max_el = table[i][j]
                tple = (i, j)

    return second[tple[1] - max_el:tple[1]]
#print(longest("The quick brown fox jumps over the lazy dog", "A fox which is quick and brown jumps over the dog which is lazy"))
print(longest("alabalala", "blalala"))
