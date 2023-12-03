# You are given an integer array nums. A number x is lonely when it appears only once, and no adjacent numbers (i.e. x + 1 and x - 1) appear in the array.

# Return all lonely numbers in nums. You may return the answer in any order.

from collections import Counter
class Solution:
    def findLonely(self, nums):
        c = dict(Counter(nums))
        # print(c)
        ans = []
        for i,j in c.items():
            if j == 1:
                x = i-1
                y = i+1
                if x not in c.keys() and y not in c.keys():
                    ans.append(i)
            else:
                continue
        return ans
    
s = Solution()
nums = [10,6,5,8]
print(s.findLonely(nums))