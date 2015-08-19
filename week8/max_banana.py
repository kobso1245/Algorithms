def max_ban(matrix, n):

    for i in range(1,n):
        matrix[n-1][i] += maxtrix[n-1][i-1]
    for i in range(n-2,-1,-1):
        matrix[i][0] += matrix[i+1][0]
    for i in range(n-2, -1, -1):
        for j in range(1, n):
            matrix[i][j] = max(matrix[i+1][j], matrix[i][j-1]) + matrix[i][j]

    return matrix[0][n-1]

maxtrix = [[9,3,4,1,5],
           [1,7,1,9,1],
           [4,2,1,3,4],
           [2,1,2,2,1],
           [1,3,2,1,7]]

print(max_ban(maxtrix,5))
