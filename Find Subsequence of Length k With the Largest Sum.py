# You are given an integer array nums and an integer k. You want to find a subsequence of nums of length k that has the largest sum.

# Return any such subsequence as an integer array of length k.

# A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

class Solution:
    def maxSubsequence(self, nums, k):
        while len(nums)>k:
            nums.remove(min(nums))
        return nums
    
s = Solution()
nums = [2,1,3,3]
k = 2
print(s.maxSubsequence(nums, k))