class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        wordc = {}
        
        for c in text:
            if c not in wordc:
                wordc[c] = 1
            else:
                wordc[c] += 1
        word = "balloon"
        cnt = 0
        while 'b' in wordc and wordc['b'] >= 1:
            found = False
            for c in word:
                if c in wordc and wordc[c] >= 1:
                    wordc[c] -= 1
                else:
                    found = True
                    break
            if not found:
                cnt += 1
            else:
                break
        
        return cnt
        
