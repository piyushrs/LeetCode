# import time
class Solution:
    def containsDuplicate(self, nums) -> bool:
        counts = dict()
        for i in nums:
            if i not in counts.keys():
                counts[i] = 1
            else:
                return True
        return False
    
# start = time.time()
s = Solution()
nums = [1,2,3,4]
print(s.containsDuplicate(nums))
# print(f"Total time taken: {time.time() - start}")