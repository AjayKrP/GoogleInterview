class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i=0
        j=0
        n=len(s)
        m=len(t)
        while i < m and j < n:
            if j==n:
                return True
            if(t[i]==s[j]):
                j += 1
            i += 1
        return j==n
