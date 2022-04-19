class Solution:
    def reverse_word(self, word) -> str:
        stack = []
        # convert string to character array
        word = list(word)
        for c in word:
            # Add all character to stack
            stack.append(c)
        for i in range(len(word)):
            # Pop element and add it to the current index
            word[i] = stack.pop()
        # Now join the character array and return
        return ''.join(word)

sol = Solution()
print(sol.reverse_word("literacis"))