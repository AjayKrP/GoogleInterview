class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        maps = {}
        pattern = list(pattern)
        s = s.split(' ')
        if len(s) != len(pattern):
            return False
        for i, word in enumerate(s):
            if pattern[i] not in maps:
                if word not in maps.values():
                    maps[pattern[i]] = word
                else:
                    return False
            elif maps[pattern[i]] != word:
                return False
        
        return True
        
        
        
