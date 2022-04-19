class Solution:
    def get_reverse(self, curr):
        if curr == '}':
            return '{'
        if curr == ')':
            return '('
        if curr == ']':
            return '['
        return curr

    def isValid(self, s: str) -> bool:
        stack = []
        s = list(s)
        for char in s:
            if char == '[' or char == '(' or char == '{':
                stack.append(char)
            else:
                if len(stack) and self.get_reverse(char) == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
