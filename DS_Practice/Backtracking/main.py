class Backtracking:
    def find_subset(self, nums, start, track, res):
        res.append(track[:])
        for i in range(start, len(nums)):
            track.append(nums[i])
            self.find_subset(nums, i + 1, track, res)
            track.pop()

    def find_combination(self, n, k, start, track):
        if k == len(track):
            res.append(track[:])
            return
        for i in range(start, n + 1):
            track.append(i)
            self.find_combination(n, k, i + 1, track)
            track.pop()

    def find_permutations(self, nums, track):
        if len(nums) == len(track):
            res.append(track[:])
            return
        for i in range(len(nums)):
            if nums[i] in track:
                continue
            track.append(nums[i])
            self.find_permutations(nums, track)
            track.pop()

    def find_permutations_by_swapping(self, a, l, r):
        if l == r:
            print(a)
            return
        else:
            for i in range(l, r + 1):
                a[l], a[i] = a[i], a[l]
                self.find_permutations_by_swapping(a, l + 1, r)
                a[l], a[i] = a[i], a[l]  # backtrack
            

bt = Backtracking()
res = []
bt.find_subset([1, 2, 3], 0, [], res)
print(res)

# res = []
# n = 4
# k = 2
# bt.find_combination(n, k, 1, [])
# print(res)

res = []
bt.find_permutations_by_swapping([1,2,3], 0, 2)
print(res)