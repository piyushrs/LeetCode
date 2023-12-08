class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        num_dic = dict()
        for i in range(n):
          temp = target-nums[i]
          if temp in num_dic.keys():
            return [i, num_dic[temp]]
          num_dic[nums[i]] = i
        return None
    
nums = [2,7,11,15]
target = 9
s = Solution()
print(s.twoSum(nums, target))