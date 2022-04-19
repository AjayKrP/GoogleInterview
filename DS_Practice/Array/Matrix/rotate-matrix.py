def rotate_matrix(mat):
    m = len(mat)
    n = len(mat[0])

    left = 0
    right = n - 1

    top = 0
    bottom = m - 1

    while left < right and top < bottom:
        prev = mat[top + 1][left]
        for i in range(left, right + 1):
            curr = mat[top][i]
            mat[top][i] = prev
            prev = curr
        top += 1

        for i in range(top, bottom + 1):
            curr = mat[i][right]
            mat[i][right] = prev
            prev = curr

        right -= 1

        for i in range(right, left - 1, -1):
            curr = mat[bottom][i]
            mat[bottom][i] = prev
            prev = curr
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            curr = mat[i][left]
            mat[i][left] = prev
            prev = curr
        left += 1

    return mat


print(rotate_matrix([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]))

print(rotate_matrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
