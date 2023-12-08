# You are given an array nums that consists of non-negative integers. Let us define rev(x) as the reverse of the non-negative integer x. For example, rev(123) = 321, and rev(120) = 21. A pair of indices (i, j) is nice if it satisfies all of the following conditions:

# 1. 0 <= i < j < nums.length
# 2. nums[i] + rev(nums[j]) == nums[j] + rev(nums[i])

# Return the number of nice pairs of indices. Since that number can be too large, return it modulo 10**9 + 7.

from collections import defaultdict
class Solution:
    def __init__(self):
        self.revs = dict()

    def getRev(self, n):
        if n not in self.revs.keys():
            return int(str(n)[::-1])
        
        return self.revs[n]

    def countNicePairs(self, nums):
        n = len(nums)
        count = 0
        arr = []
        for i in nums:
            if i not in self.revs.keys():
                x = self.getRev(i)
                arr.append(i - x)
                self.revs[i] = x
            else:
                arr.append(i - self.revs[i])
        
        md = 10**9 + 7
        d = defaultdict(int)
        for i in arr:
            count = (count + d[i]) % md
            d[i] += 1
        
        return count
    
s = Solution()
nums = [42,11,1,97]
print(s.countNicePairs(nums))