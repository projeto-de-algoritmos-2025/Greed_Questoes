class Solution(object):
    def minPatches(self, nums, n):
        patches = 0
        x = 1
        i = 0
        while x <= n:
            if i < len(nums) and nums[i] <= x:
                x += nums[i]
                i += 1
            else:
                x *= 2
                patches += 1
        return patches
