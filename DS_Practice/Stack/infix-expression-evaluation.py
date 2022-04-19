class Solution:

    def calculate(self, s: str):

        def update(op, v):
            if op == "+": return stack.append(v)
            if op == "-": return stack.append(-v)
            if op == '*': return stack.append(stack.pop()*v)
            if op == '/': return stack.append(stack.pop()/v)

        it, num, stack, sign = 0, 0, [], '+'

        while it < len(s):
            if s[it].isdigit():
                num = (num*10) + int(s[it])
            elif s[it] in "+-*/":
                update(s[it], num)
                num, sign = 0, s[it]
            elif s[it] == '(':
                num, j = self.calculate(s[it + 1:])
                it = it + j
            elif s[it] == ')':
                update(sign, num)
                return sum(stack), it + 1
            it += 1

        update(sign, num)
        return sum(stack)