def max_sum(matrix):
    m = len(matrix)
    n = len(matrix[0])
    gmax = float('-inf')
    for i in range(1, m - 1):
        for j in range(1, n - 1):
            tsum = matrix[i - 1][j - 1] + matrix[i - 1][j] + matrix[i - 1][j + 1] + \
                   matrix[i][j] + matrix[i + 1][j - 1] + matrix[i + 1][j] + matrix[i + 1][j + 1]
            gmax = max(gmax, tsum)
    return gmax


# Driver Code
arr = [[1, 2, 3, 0, 0],
       [0, 0, 0, 0, 0],
       [2, 1, 4, 0, 0],
       [0, 0, 0, 0, 0],
       [1, 1, 0, 1, 0]]
print(max_sum(arr))
