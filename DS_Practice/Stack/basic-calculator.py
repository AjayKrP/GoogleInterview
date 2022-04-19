class Solution:
    def calculate(self, s: str) -> int:
        def helper(s):
            stack = []
            sign = '+'
            res = 0
            while len(s) > 0:
                c = s.pop(0)
                if c.isdigit():
                    res = res * 10 + int(c)
                if c == '(':
                    res = helper(s)
                if (not c.isdigit() and c != ' ') or 0 == len(s):
                    if sign == '+':
                        stack.append(res)
                    elif sign == '-':
                        stack.append(-1 * res)
                    elif sign == '*':
                        val = stack.pop()
                        stack.append(val * res)
                    elif sign == '/':
                        val = stack.pop()
                        stack.append(val // res)
                    sign = c
                    res = 0
                if c == ')':
                    break
            return sum(stack)

        return helper(list(s))
