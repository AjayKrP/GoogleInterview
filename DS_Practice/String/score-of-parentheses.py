class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        i = 0
        res = 0
        stack.append(0)
        while i < len(s):
            if s[i] == '(':
                stack.append(0)
            else:
                v = stack.pop()
                w = stack.pop()
                stack.append(w + max(2 * v, 1))
            i += 1
        return stack.pop()
