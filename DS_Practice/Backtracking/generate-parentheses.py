class Solution:
    def is_balanced(self, word):
        stack = []
        for current in word:
            if current == '(':
                stack.append(current)
            elif current == ')':
                if len(stack) and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

    def generateParenthesis(self, n: int):
        def helper(track, res):
            if len(track) == 2 * n:
                tmp = ''.join(track[:])
                if self.is_balanced(track) and tmp not in res:
                    res.append(res)
                return

            for c in '()':
                helper(track + [c], res)

        res = []
        helper([], res)
        return res


sol = Solution()
print(sol.generateParenthesis(3))
