class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        
        bal = 0
        res = ''
        tmp = ''
        indx = 0
        for i in range(len(s)):
            tmp += s[i]
            if s[i] == '(':
                bal += 1
            else:
                bal -= 1
            
            if bal == 0:
                res += tmp[1:-1]
                tmp = ''
        return res
