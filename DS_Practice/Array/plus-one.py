class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits) - 1
        carry, out = divmod(digits[n] + 1, 10)
        j = n

        digits[n] = out

        j = n - 1

        while carry and j >= 0:
            carry, out = divmod(digits[j] + carry, 10)
            digits[j] = out
            j -= 1
        if carry:
            digits.insert(0, carry)
        return digits