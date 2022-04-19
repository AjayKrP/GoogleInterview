
from collections import OrderedDict

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        
        def get_name_dict(val):
            left = 0
            n = len(val)
            val = list(val)
            res = []
            curr = 0
            while left < n:
                right = left + 1
                while right < n and val[left] == val[right]:
                    right += 1
                
                res.append((val[left], right - left))
                
                left = right
            return res
        res1 = get_name_dict(name)
        res2 = get_name_dict(typed)
        print(res1)
        print(res2)
        if len(res1) != len(res2):
            return False
        for i, item in enumerate(res2):
            if res1[i][0] != item[0] or res1[i][1] > item[1]:
                return False
        return True
