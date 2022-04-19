class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        items = {}

        # Count frequency of elements
        for ele in nums:
            if ele in items:
                items[ele] += 1
            else:
                items[ele] = 1

        # Sort elements in decending by key
        items = dict(sorted(items.items(), reverse=True))  # sort by a
        # Now sort elements in ascending order by frequency which means value
        items = dict(sorted(items.items(), key=lambda x: x[1]))

        # Now add final dictionary to result array and return
        res = []
        for key in items:
            res += [key] * items[key]
        return res