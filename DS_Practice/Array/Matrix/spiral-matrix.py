class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        #         top = left = 0
        #         m = len(matrix)
        #         n = len(matrix[0])
        #         right = n
        #         bottom = m

        #         res = []
        #         visited = [[False for _ in range(n)] for _ in range(m)]
        #         while top < bottom and left < right:
        #             print(top,bottom,left,right)
        #             for i in range(left, right):
        #                 if not visited[top][i]:
        #                     res.append(matrix[top][i])
        #                     visited[top][i] = True

        #             top += 1

        #             for i in range(top, bottom):
        #                 if visited[i][right-1]:
        #                     res.append(matrix[i][right-1])
        #                     visited[i][right-1] = True

        #             right -= 1

        #             for i in range(right-1, left - 1, -1):
        #                 if not visited[bottom-1][i]:
        #                     res.append(matrix[bottom-1][i])
        #                     visited[bottom-1][i] = True

        #             bottom -= 1

        #             for i in range(bottom-1, top-1, -1):
        #                 if not visited[i][left]:
        #                     res.append(matrix[i][left])
        #                     visited[i][left] = True

        #             left += 1

        #         return res
        ans = []

        m = len(matrix)
        n = len(matrix[0])

        left, right, up, down = 0, n, 0, m

        i, j = 0, 0

        while down > up and right > left:

            while j < right - 1:
                ans.append(matrix[i][j])
                j += 1
            up += 1

            while i < down - 1:
                ans.append(matrix[i][j])
                i += 1
            right -= 1

            if left == right or up == down:
                ans.append(matrix[i][j])
                break

            while j > left:
                ans.append(matrix[i][j])
                j -= 1
            down -= 1

            while i > up:
                ans.append(matrix[i][j])
                i -= 1
            left += 1

            if left == right or up == down:
                ans.append(matrix[i][j])
                break

        return ans
