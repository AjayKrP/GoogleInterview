class Solution:
    def dp(self, s, index, lookup, decoders):
        # If all the characters of s can be completely decoded then we have found a way.
        if index == len(s):
            return 1

        # Memoization
        if lookup[index] == -1:
            # Variable to store the number of ways s can be decoded.
            ways = 0
            for i in range(index, len(s)):
                # If characters from index till i can be decoded then check for the remaining characters of s, whether they can be decoded or not. If yes then we add 1 to our ways.
                if s[index:i + 1] in decoders:
                    ways += self.dp(s, i + 1, lookup, decoders)
            lookup[index] = ways
        return lookup[index]

    def numDecodings(self, s: str) -> int:
        # decoders => ("1", "2", "3", ..., "26")
        return self.dp(s, 0, [-1 for _ in range(len(s))], set([str(i) for i in range(1, 27)]))