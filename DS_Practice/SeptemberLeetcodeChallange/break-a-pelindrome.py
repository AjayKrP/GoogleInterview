class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        res = ""
        for i in range(len(palindrome)):
            check = ord(palindrome[i]) - ord('a')
            tmp = palindrome
            if check > 0:
                tmp = list(tmp)
                tmp[i] = 'a'
                if tmp == tmp[::-1]:
                    continue
                else:
                    return ''.join(tmp)
        tmp = list(palindrome)
        tmp[len(palindrome) - 1] = chr(ord(tmp[len(palindrome) - 1]) + 1)
        return "".join(tmp) if len(palindrome) > 1  else ""
